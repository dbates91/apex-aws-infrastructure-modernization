# Python Operations

`check_docs.py` verifies that the project-documentation scaffold contains required paths. It is read-only, uses only the Python standard library, and does **not** interact with AWS.

Example: `python3 scripts/python/check_docs.py`.

Future scripts may use boto3 for **explicitly scoped, read-only** inventory and CloudWatch checks, with documented IAM permissions, redaction, tests and cost considerations.

