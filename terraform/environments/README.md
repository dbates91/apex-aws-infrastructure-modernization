# Terraform environments

Each environment is an independent Terraform root with explicitly reviewed state isolation and variable values. Currently only [dev](dev/README.md) exists and declares **no provisioned resources**.

Do not reuse state between environments or commit generated state files. Select the intended AWS account and Region before a future real plan or deployment.

