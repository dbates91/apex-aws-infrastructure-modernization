#!/usr/bin/env python3
"""Read-only, opt-in AWS CLI inventory for Apex-tagged EC2 instances."""
import argparse
import json
import subprocess


def build_command(profile: str, region: str) -> list[str]:
    if not profile or not region or not all(c.isalnum() or c in "_-." for c in profile + region):
        raise ValueError("Specify simple non-empty AWS profile and Region names")
    return [
        "aws", "--profile", profile, "--region", region,
        "ec2", "describe-instances",
        "--filters", "Name=tag:Project,Values=Apex",
        "--query", "Reservations[].Instances[].State.Name",
        "--output", "json",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, help="Explicit named AWS CLI profile")
    parser.add_argument("--region", required=True, help="Explicit AWS Region")
    parser.add_argument("--execute", action="store_true", help="Allow read-only API query")
    args = parser.parse_args()
    try:
        cmd = build_command(args.profile, args.region)
    except ValueError as exc:
        parser.error(str(exc))
    if not args.execute:
        print("DRY RUN: would make an EC2 DescribeInstances read-only query for Project=Apex.")
        print("No AWS API call made. Pass --execute only after reviewing scope/permissions.")
        return 0
    try:
        output = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=30)
        states = json.loads(output.stdout)
        if not isinstance(states, list):
            raise ValueError("Unexpected AWS CLI response")
    except (subprocess.SubprocessError, OSError, json.JSONDecodeError, ValueError):
        print("Inventory failed; check credentials, permissions, Region, and CLI setup.")
        return 1
    counts = {}
    for state in states:
        if not isinstance(state, str):
            return 1
        counts[state] = counts.get(state, 0) + 1
    print(f"Apex-tagged EC2 instance count: {len(states)}")
    for state, amount in sorted(counts.items()):
        print(f"{state}: {amount}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
