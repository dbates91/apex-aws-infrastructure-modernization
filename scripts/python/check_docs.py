#!/usr/bin/env python3
"""Read-only local check of required Apex repository documentation paths."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = (
    "README.md",
    ".gitignore",
    "PROJECT_ROADMAP.md",
    "PROJECT_TRACKER.md",
    "COST_MANAGEMENT.md",
    "LEARNING_OBJECTIVES.md",
    "SECURITY.md",
    "architecture/README.md",
    "terraform/README.md",
    "terraform/environments/README.md",
    "terraform/modules/README.md",
    "linux/README.md",
    "docker/README.md",
    "application/README.md",
    "scripts/README.md",
    "docs/README.md",
    "docs/deployment/README.md",
    "docs/troubleshooting/README.md",
    "docs/runbooks/README.md",
    "docs/architecture-decisions/README.md",
    "screenshots/README.md",
)

def main() -> int:
    missing = [relative for relative in REQUIRED if not (ROOT / relative).is_file()]
    if missing:
        for relative in missing:
            print(f"MISSING: {relative}")
        return 1
    print(f"All {len(REQUIRED)} required documentation paths exist locally.")
    print("This does not verify AWS resource deployment or Terraform configuration.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

