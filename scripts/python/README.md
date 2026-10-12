# Python operations and verification

- [check_docs.py](check_docs.py): local read-only required-path check.
- [estimate_costs.py](estimate_costs.py): offline cost arithmetic using **user-provided verified unit rates**, with no AWS calls. See [pricing template](../../docs/costs/pricing-input.example.json).
- [inventory_ec2.py](inventory_ec2.py): explicit-profile/Region *read-only* AWS CLI query tool; **dry-run by default** and never assumes credentials or a running Apex deployment.

Offline tests: `python3 -m unittest discover -s tests -p 'test_*.py' -v` from repository root.

Later operational scripts should follow least privilege, request explicit scope, have bounded retries, sanitize results, never leak secrets or silently mutate AWS.
