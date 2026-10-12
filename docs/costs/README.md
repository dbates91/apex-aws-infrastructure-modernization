# Offline AWS cost experiment planning

Use `scripts/python/estimate_costs.py` with a locally populated JSON input describing quantities and **verified, current, Region-specific unit prices**. This helper performs arithmetic; it does **not** fetch real AWS prices or inspect billing.

The example JSON uses `null` prices intentionally. Fill in real AWS Pricing Calculator/current published rates privately before using it. Never publish private account identifiers. Record observed charges after AWS billing settles, accounting for lag.
