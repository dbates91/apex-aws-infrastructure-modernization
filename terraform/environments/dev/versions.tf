terraform {
  required_version = ">= 1.10.0, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0, < 7.0"
    }
  }
}

# Safe root: no AWS resources, data sources, backend, or module calls.
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
