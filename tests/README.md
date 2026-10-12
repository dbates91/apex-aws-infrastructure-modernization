# Offline tests

`test_application.py` runs HTTP functional tests using a local ephemeral port and standard-library `unittest`. No AWS account or deployed services are needed.

Run from the repository root:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

A passing offline test verifies the sample application handler but does **not** verify the AWS architecture, Terraform code, Docker image, security groups or load balancing.
