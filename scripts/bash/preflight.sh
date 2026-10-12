#!/usr/bin/env bash
set -euo pipefail

# Local-only dependency preflight. No network calls, AWS API actions, or provisioning.
echo "Apex local tool preflight (no AWS services accessed)"
missing=0
for tool in git terraform aws python3 docker; do
  if command -v "$tool" >/dev/null 2>&1; then
    printf '[found]   %s\n' "$tool"
  else
    printf '[missing] %s\n' "$tool"
    missing=1
  fi
done
if [[ "$missing" -ne 0 ]]; then
  echo "One or more optional/lab dependencies are missing."
  exit 1
fi
echo "Required lab commands are available; no environment validation has been performed."

