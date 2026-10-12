#!/usr/bin/env python3
"""Validate and analyse coded correction-effort study records.

The input belongs in private storage. This tool reports aggregate results and
index-based validation errors; it never prints participant or output IDs.
"""

from collections import Counter, defaultdict
from datetime import date
import argparse
import json
import math
from pathlib import Path
import random
import statistics
import sys


CONDITIONS = ("none", "released-0.4.2", "candidate")
SEVERITIES = ("critical", "consequential", "minor", "preference")
PHASE_CONDITIONS = {
    "baseline": ("none", "released-0.4.2"),
    "candidate-pilot": CONDITIONS,
    "confirmatory": CONDITIONS,
}
PHASE_SAMPLE_RANGE = {
    "baseline": (12, 12),
    "candidate-pilot": (6, 8),
    "confirmatory": (36, 120),
}
REGRESSIONS = {
    "privacy",
    "historical-evidence",
    "modern-product-boundary",
    "low-energy-interaction",
    "deliverable-completion",
    "document-safety",
}
ROOT_FIELDS = {
    "schema_version",
    "study_id",
    "phase",
    "generated_on",
    "protocol_frozen",
    "review_complete_before_unblinding",
    "accessibility_time_exception",
    "regressions",
    "outputs",
}
OUTPUT_FIELDS = {
    "output_id",
    "participant_id",
    "task_id",
    "task_family",
    "condition",
    "condition_order",
    "elapsed_seconds",
    "completion_status",
    "requested_deliverable_complete",
    "blocking_questions",
    "effort_rating",
    "accurate_representation",
    "disclosure_control",
    "reviewer_ids",
    "actions",
}
ACTION_FIELDS = {"action_id", "reviewer_1", "reviewer_2", "adjudicated"}


def _valid_date(value):
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return len(value) == 10


def _is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _balanced(counter, labels):
    values = [counter.get(label, 0) for label in labels]
    return max(values) - min(values) <= 1


def validate_record(record):
    """Return index-based errors for a coded study record."""
    errors = []
    if not isinstance(record, dict):
        return ["Study record must be an object."]
    if set(record) != ROOT_FIELDS:
        errors.append("Study record fields differ from the data contract.")
    if record.get("schema_version") != 1 or record.get("study_id") != "correction-effort-v1":
        errors.append("Study identity or schema version is invalid.")
    phase = record.get("phase")
    expected_conditions = PHASE_CONDITIONS.get(phase)
    if expected_conditions is None:
        errors.append("Study phase must be baseline, candidate-pilot or confirmatory.")
        expected_conditions = ()
    if not _valid_date(record.get("generated_on")):
        errors.append("Generated date must be a valid ISO calendar date.")
    if not isinstance(record.get("protocol_frozen"), bool):
        errors.append("protocol_frozen must be boolean.")
    if phase == "confirmatory" and record.get("protocol_frozen") is not True:
        errors.append("Confirmatory analysis requires a frozen protocol.")
    if record.get("review_complete_before_unblinding") is not True:
        errors.append("Reviews must be complete before condition unblinding.")

    exception = record.get("accessibility_time_exception")
    if not isinstance(exception, dict) or set(exception) != {"applies", "basis"}:
        errors.append("Accessibility time exception must contain applies and basis.")
    else:
        if not isinstance(exception.get("applies"), bool):
            errors.append("Accessibility time exception applies must be boolean.")
        if exception.get("applies") and (not isinstance(exception.get("basis"), str) or not exception["basis"].strip()):
            errors.append("An accessibility time exception requires a recorded basis.")

    regressions = record.get("regressions")
    if not isinstance(regressions, dict) or set(regressions) != REGRESSIONS:
        errors.append("Regression results differ from the required set.")
    elif any(value not in {"pass", "fail", "pending"} for value in regressions.values()):
        errors.append("Regression results must be pass, fail or pending.")

    outputs = record.get("outputs")
    if not isinstance(outputs, list) or not outputs:
        return errors + ["Study outputs must be a non-empty list."]

    seen_outputs = set()
    participants = defaultdict(list)
    for index, output in enumerate(outputs):
        prefix = f"outputs[{index}]"
        if not isinstance(output, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        if set(output) != OUTPUT_FIELDS:
            errors.append(f"{prefix} fields differ from the data contract.")
            continue
        for key in ("output_id", "participant_id", "task_id", "task_family"):
            if not isinstance(output[key], str) or not output[key].strip():
                errors.append(f"{prefix}.{key} must be non-empty text.")
        output_id = output.get("output_id")
        if output_id in seen_outputs:
            errors.append(f"{prefix}.output_id is duplicated.")
        seen_outputs.add(output_id)
        condition = output.get("condition")
        if condition not in expected_conditions:
            errors.append(f"{prefix}.condition is not valid for this phase.")
        if not isinstance(output.get("condition_order"), int) or isinstance(output.get("condition_order"), bool):
            errors.append(f"{prefix}.condition_order must be an integer.")
        if not _is_number(output.get("elapsed_seconds")) or output["elapsed_seconds"] <= 0:
            errors.append(f"{prefix}.elapsed_seconds must be positive.")
        if output.get("completion_status") not in {"completed", "candidate-controlled-pause"}:
            errors.append(f"{prefix}.completion_status is invalid.")
        if not isinstance(output.get("requested_deliverable_complete"), bool):
            errors.append(f"{prefix}.requested_deliverable_complete must be boolean.")
        if not isinstance(output.get("blocking_questions"), int) or isinstance(output.get("blocking_questions"), bool) or output["blocking_questions"] < 0:
            errors.append(f"{prefix}.blocking_questions must be a non-negative integer.")
        effort = output.get("effort_rating")
        if effort is not None and (not isinstance(effort, int) or isinstance(effort, bool) or not 1 <= effort <= 7):
            errors.append(f"{prefix}.effort_rating must be null or an integer from 1 to 7.")
        for key in ("accurate_representation", "disclosure_control"):
            if output.get(key) not in {"yes", "no", "skipped"}:
                errors.append(f"{prefix}.{key} must be yes, no or skipped.")
        reviewers = output.get("reviewer_ids")
        if not isinstance(reviewers, list) or len(reviewers) != 2 or len(set(reviewers)) != 2 or not all(isinstance(v, str) and v.strip() for v in reviewers):
            errors.append(f"{prefix}.reviewer_ids must contain two distinct coded reviewers.")

        actions = output.get("actions")
        if not isinstance(actions, list):
            errors.append(f"{prefix}.actions must be a list.")
        else:
            seen_actions = set()
            for action_index, action in enumerate(actions):
                action_prefix = f"{prefix}.actions[{action_index}]"
                if not isinstance(action, dict) or set(action) != ACTION_FIELDS:
                    errors.append(f"{action_prefix} fields differ from the data contract.")
                    continue
                action_id = action.get("action_id")
                if not isinstance(action_id, str) or not action_id.strip() or action_id in seen_actions:
                    errors.append(f"{action_prefix}.action_id must be unique non-empty text within the output.")
                seen_actions.add(action_id)
                for key in ("reviewer_1", "reviewer_2", "adjudicated"):
                    if action.get(key) not in SEVERITIES:
                        errors.append(f"{action_prefix}.{key} has an invalid severity.")
        participant_id = output.get("participant_id")
        if isinstance(participant_id, str) and participant_id.strip():
            participants[participant_id].append(output)

    if expected_conditions:
        required_orders = set(range(1, len(expected_conditions) + 1))
        for participant_index, participant_outputs in enumerate(participants.values()):
            if len(participant_outputs) != len(expected_conditions):
                errors.append(f"participant[{participant_index}] does not have one output per condition.")
                continue
            if {o.get("condition") for o in participant_outputs} != set(expected_conditions):
                errors.append(f"participant[{participant_index}] condition set is incomplete or duplicated.")
            if {o.get("condition_order") for o in participant_outputs} != required_orders:
                errors.append(f"participant[{participant_index}] condition order is incomplete or duplicated.")
            if len({o.get("task_id") for o in participant_outputs}) != len(participant_outputs):
                errors.append(f"participant[{participant_index}] repeats a source packet.")
            if len({o.get("task_family") for o in participant_outputs}) != len(participant_outputs):
                errors.append(f"participant[{participant_index}] repeats a task family.")

        minimum, maximum = PHASE_SAMPLE_RANGE[phase]
        if not minimum <= len(participants) <= maximum:
            errors.append(f"{phase} requires {minimum}" + (f" to {maximum}" if minimum != maximum else "") + " complete participants.")

    if phase == "confirmatory" and not errors:
        for family in {o["task_family"] for o in outputs}:
            counts = Counter(o["condition"] for o in outputs if o["task_family"] == family)
            if not _balanced(counts, CONDITIONS):
                errors.append("Task-family assignment is not balanced across conditions.")
                break
        for order in (1, 2, 3):
            counts = Counter(o["condition"] for o in outputs if o["condition_order"] == order)
            if not _balanced(counts, CONDITIONS):
                errors.append("Condition order is not counterbalanced.")
                break
    return errors


def _action_counts(output):
    counts = Counter(action["adjudicated"] for action in output["actions"])
    return {severity: counts.get(severity, 0) for severity in SEVERITIES}


def _mean(values):
    return statistics.fmean(values) if values else None


def _rate(values):
    return _mean([1.0 if value else 0.0 for value in values])


def _yes_rate(outputs, key):
    values = [o[key] == "yes" for o in outputs if o[key] != "skipped"]
    return _rate(values)


def _normal_one_sided_p(mean_difference, standard_error):
    if standard_error == 0:
        return 0.0 if mean_difference < 0 else 1.0
    return statistics.NormalDist().cdf(mean_difference / standard_error)


def _holm_adjust(p_values):
    ordered = sorted(enumerate(p_values), key=lambda item: item[1])
    adjusted = [0.0] * len(p_values)
    running = 0.0
    total = len(p_values)
    for rank, (original_index, value) in enumerate(ordered):
        running = max(running, min(1.0, (total - rank) * value))
        adjusted[original_index] = running
    return adjusted


def _paired_differences(outputs, control):
    by_participant = defaultdict(dict)
    for output in outputs:
        counts = _action_counts(output)
        by_participant[output["participant_id"]][output["condition"]] = counts["consequential"]
    return [values["candidate"] - values[control] for values in by_participant.values()]


def _contrast_statistics(outputs):
    controls = ("none", "released-0.4.2")
    raw = []
    for control in controls:
        differences = _paired_differences(outputs, control)
        mean_difference = _mean(differences)
        standard_error = statistics.stdev(differences) / math.sqrt(len(differences)) if len(differences) > 1 else 0.0
        raw.append({
            "control": control,
            "participants": len(differences),
            "candidate_minus_control": mean_difference,
            "mean_reduction": -mean_difference,
            "standard_error": standard_error,
            "one_sided_p_value": _normal_one_sided_p(mean_difference, standard_error),
        })
    adjusted = _holm_adjust([item["one_sided_p_value"] for item in raw])
    simultaneous_z = statistics.NormalDist().inv_cdf(1 - 0.05 / len(raw))
    for item, adjusted_p in zip(raw, adjusted):
        item["holm_adjusted_p_value"] = adjusted_p
        item["simultaneous_95_upper_bound"] = item["candidate_minus_control"] + simultaneous_z * item["standard_error"]
        item["primary_gate"] = (
            item["mean_reduction"] >= 0.5
            and item["holm_adjusted_p_value"] < 0.05
            and item["simultaneous_95_upper_bound"] < 0
        )
    return raw


def analyse(record):
    """Return aggregate descriptive results and the confirmatory gate."""
    outputs = record["outputs"]
    summaries = {}
    for condition in PHASE_CONDITIONS[record["phase"]]:
        selected = [o for o in outputs if o["condition"] == condition]
        counts = [_action_counts(output) for output in selected]
        effort = [o["effort_rating"] for o in selected if o["effort_rating"] is not None]
        summaries[condition] = {
            "outputs": len(selected),
            "mean_consequential_corrections": _mean([c["consequential"] for c in counts]),
            "critical_failures": sum(c["critical"] for c in counts),
            "usable_without_critical_or_consequential_correction_rate": _rate([
                output["requested_deliverable_complete"] and counts[index]["critical"] == 0 and counts[index]["consequential"] == 0
                for index, output in enumerate(selected)
            ]),
            "mean_elapsed_seconds": _mean([o["elapsed_seconds"] for o in selected]),
            "mean_blocking_questions": _mean([o["blocking_questions"] for o in selected]),
            "mean_effort_rating": _mean(effort),
            "deliverable_complete_rate": _rate([o["requested_deliverable_complete"] for o in selected]),
            "accurate_representation_yes_rate": _yes_rate(selected, "accurate_representation"),
            "disclosure_control_yes_rate": _yes_rate(selected, "disclosure_control"),
        }

    action_pairs = [
        (action["reviewer_1"], action["reviewer_2"])
        for output in outputs for action in output["actions"]
    ]
    agreement = _rate([left == right for left, right in action_pairs]) if action_pairs else None
    result = {
        "study_id": record["study_id"],
        "phase": record["phase"],
        "participants": len({o["participant_id"] for o in outputs}),
        "condition_summaries": summaries,
        "reviewer_exact_severity_agreement": agreement,
        "contrasts": [],
        "release_gate": {"evaluated": False, "passed": None, "checks": {}},
    }
    if "candidate" not in PHASE_CONDITIONS[record["phase"]]:
        return result

    contrasts = _contrast_statistics(outputs)
    result["contrasts"] = contrasts
    if record["phase"] != "confirmatory":
        return result

    checks = {}
    checks["primary_against_both_controls"] = all(item["primary_gate"] for item in contrasts)
    candidate = summaries["candidate"]
    for control in ("none", "released-0.4.2"):
        checks[f"zero_correction_gain_vs_{control}"] = (
            candidate["usable_without_critical_or_consequential_correction_rate"]
            - summaries[control]["usable_without_critical_or_consequential_correction_rate"]
            >= 0.15
        )
        checks[f"time_vs_{control}"] = (
            record["accessibility_time_exception"]["applies"]
            or candidate["mean_elapsed_seconds"] <= summaries[control]["mean_elapsed_seconds"] * 1.10
        )
    checks["no_candidate_critical_failures"] = candidate["critical_failures"] == 0
    checks["all_regressions_pass"] = all(value == "pass" for value in record["regressions"].values())
    result["release_gate"] = {"evaluated": True, "passed": all(checks.values()), "checks": checks}
    return result


def simulate_power(record, iterations=5000, seed=20261012):
    """Estimate confirmatory power by resampling complete participant blocks."""
    outputs = record["outputs"]
    by_participant = defaultdict(dict)
    for output in outputs:
        by_participant[output["participant_id"]][output["condition"]] = _action_counts(output)["consequential"]
    blocks = [
        (values["candidate"] - values["none"], values["candidate"] - values["released-0.4.2"])
        for values in by_participant.values()
    ]
    rng = random.Random(seed)
    estimates = []
    for sample_size in range(36, 121):
        passes = 0
        for _ in range(iterations):
            sample = [blocks[rng.randrange(len(blocks))] for _ in range(sample_size)]
            contrast_results = []
            p_values = []
            for position in (0, 1):
                differences = [pair[position] for pair in sample]
                mean_difference = _mean(differences)
                standard_error = statistics.stdev(differences) / math.sqrt(sample_size)
                p_value = _normal_one_sided_p(mean_difference, standard_error)
                p_values.append(p_value)
                contrast_results.append((mean_difference, standard_error))
            adjusted = _holm_adjust(p_values)
            simultaneous_z = statistics.NormalDist().inv_cdf(0.975)
            if all(
                -mean_difference >= 0.5
                and adjusted[index] < 0.05
                and mean_difference + simultaneous_z * standard_error < 0
                for index, (mean_difference, standard_error) in enumerate(contrast_results)
            ):
                passes += 1
        power = passes / iterations
        estimates.append({"sample_size": sample_size, "estimated_power": power})
        if power >= 0.8:
            return {
                "method": "empirical participant-block resampling",
                "iterations": iterations,
                "seed": seed,
                "pilot_participants": len(blocks),
                "recommended_completers": sample_size,
                "estimated_power": power,
                "within_protocol_bounds": True,
                "estimates": estimates,
            }
    return {
        "method": "empirical participant-block resampling",
        "iterations": iterations,
        "seed": seed,
        "pilot_participants": len(blocks),
        "recommended_completers": None,
        "estimated_power": estimates[-1]["estimated_power"],
        "within_protocol_bounds": False,
        "estimates": estimates,
    }


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate or analyse private coded correction-effort records.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "analyse"):
        child = subparsers.add_parser(command)
        child.add_argument("record", type=Path)
    power = subparsers.add_parser("power")
    power.add_argument("record", type=Path)
    power.add_argument("--iterations", type=int, default=5000)
    power.add_argument("--seed", type=int, default=20261012)
    args = parser.parse_args(argv)
    try:
        record = _load(args.record)
        errors = validate_record(record)
        if args.command == "power" and record.get("phase") != "candidate-pilot":
            errors.append("Power simulation requires a candidate-pilot record.")
        if args.command == "power" and not 100 <= args.iterations <= 100000:
            errors.append("Power iterations must be from 100 to 100000.")
        if errors:
            payload = {"status": "fail", "errors": errors}
            status = 1
        elif args.command == "validate":
            payload = {"status": "pass", "errors": []}
            status = 0
        elif args.command == "analyse":
            payload = {"status": "pass", "analysis": analyse(record)}
            status = 0
        else:
            payload = {"status": "pass", "power": simulate_power(record, args.iterations, args.seed)}
            status = 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        payload = {"status": "fail", "errors": [str(exc)]}
        status = 1
    print(json.dumps(payload, indent=2, sort_keys=True))
    return status


if __name__ == "__main__":
    sys.exit(main())
