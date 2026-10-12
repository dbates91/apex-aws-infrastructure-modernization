"""Offline command construction tests; never invoke the AWS CLI."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "python"))
from inventory_ec2 import build_command  # noqa: E402


class InventorySafetyTests(unittest.TestCase):
    def test_explicit_profile_and_region(self):
        args = build_command("lab-readonly", "us-west-2")
        self.assertEqual(args[:5], ["aws", "--profile", "lab-readonly", "--region", "us-west-2"])
        self.assertIn("describe-instances", args)
        self.assertIn("Name=tag:Project,Values=Apex", args)

    def test_command_injection_like_scope_rejected(self):
        with self.assertRaises(ValueError):
            build_command("lab;echo bad", "us-west-2")
        with self.assertRaises(ValueError):
            build_command("lab", "us-west-2 && foo")


if __name__ == "__main__":
    unittest.main()
