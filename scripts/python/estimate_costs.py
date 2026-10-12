#!/usr/bin/env python3
"""Offline cost scenario calculator; caller supplies *real* Region-specific rates."""
import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path


def cost_lines(data: dict) -> tuple[list[tuple[str, Decimal]], Decimal]:
    if data.get("currency") != "USD":
        raise ValueError("Expected currency USD")
    items = data.get("items")
    if not isinstance(items, list) or not items:
        raise ValueError("items must be a non-empty list")
    result = []
    for item in items:
        label = item.get("service")
        if not isinstance(label, str) or not label.strip():
            raise ValueError("Each item needs a service name")
        if item.get("unit_rate_usd") is None:
            raise ValueError(f"Missing verified unit_rate_usd for {label}")
        try:
            count = Decimal(str(item["units"]))
            rate = Decimal(str(item["unit_rate_usd"]))
        except (InvalidOperation, KeyError, TypeError) as exc:
            raise ValueError(f"Bad units/rate for {label}") from exc
        if not count.is_finite() or not rate.is_finite() or count < 0 or rate < 0:
            raise ValueError(f"Invalid nonnegative finite units/rate for {label}")
        result.append((label, count * rate))
    total = sum((subtotal for _, subtotal in result), Decimal("0"))
    return result, total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pricing_json", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.pricing_json.read_text(encoding="utf-8"))
        lines, total = cost_lines(data)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    for label, value in lines:
        print(f"{label}: USD {value:.4f}")
    print(f"Scenario estimate: USD {total:.4f}")
    print("Estimated from user-provided prices only; not a billing statement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
