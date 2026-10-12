variable "availability_zones" {
  description = "Exactly two distinct Availability Zone names approved for this account and Region."
  type        = list(string)

  validation {
    condition     = length(var.availability_zones) == 2 && length(distinct(var.availability_zones)) == 2
    error_message = "Provide exactly two different Availability Zone names."
  }
}

variable "project_name" {
  description = "Tag/name prefix for resources in a future approved deployment."
  type        = string
  default     = "apex"
}

variable "app_port" {
  description = "Intended application listener port (future EC2/ASG target)."
  type        = number
  default     = 8080

  validation {
    condition     = var.app_port >= 1 && var.app_port <= 65535 && floor(var.app_port) == var.app_port
    error_message = "app_port must be a valid TCP port number."
  }
}

variable "tags" {
  description = "Additional resource tags, excluding confidential identifiers."
  type        = map(string)
  default     = {}
}
