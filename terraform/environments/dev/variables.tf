variable "aws_region" {
  type        = string
  description = "Target AWS Region. The default is a placeholder, not an active deployment location."
  default     = "us-west-2"

  validation {
    condition     = length(trimspace(var.aws_region)) > 0
    error_message = "aws_region must not be empty."
  }
}

