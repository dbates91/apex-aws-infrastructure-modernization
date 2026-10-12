terraform {
  required_version = ">= 1.6.0, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0, < 7.0"
    }
  }
}

# Intentional scaffold: no AWS resources, data sources, or backend are configured.
# Authenticate with short-lived AWS credentials only when a later phase requires it.
provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "Apex"
      Environment = "dev"
      ManagedBy   = "Terraform"
    }
  }
}

