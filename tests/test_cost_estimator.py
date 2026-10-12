"""Synthetic arithmetic fixtures; not real AWS prices or bills."""
from decimal import Decimal
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "python"))
from estimate_costs import cost_lines  # noqa: E402


class CostArithmeticTests(unittest.TestCase):
    def test_two_synthetic_items(self):
        fake = {"currency": "USD", "items": [
            {"service": "fictional hourly", "units": 2, "unit_rate_usd": "0.50"},
            {"service": "fictional GB", "units": 3, "unit_rate_usd": "0.25"},
        ]}
        lines, total = cost_lines(fake)
        self.assertEqual(len(lines), 2)
        self.assertEqual(total, Decimal("1.75"))

    def test_missing_rate_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Missing verified"):
            cost_lines({"currency": "USD", "items": [
                {"service": "future billable item", "units": 1, "unit_rate_usd": None}
            ]})

    def test_negative_rate_is_rejected(self):
        with self.assertRaises(ValueError):
            cost_lines({"currency": "USD", "items": [
                {"service": "bad", "units": 1, "unit_rate_usd": "-1"}
            ]})


if __name__ == "__main__":
    unittest.main()
