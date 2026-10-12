output "vpc_id" {
  description = "Future VPC ID after authorized provisioning."
  value       = aws_vpc.this.id
}

output "public_subnet_ids" {
  description = "Future public subnet IDs keyed by AZ slot."
  value       = { for az, subnet in aws_subnet.public : az => subnet.id }
}

output "application_subnet_ids" {
  description = "Future private application subnet IDs keyed by AZ slot."
  value       = { for az, subnet in aws_subnet.application : az => subnet.id }
}

output "database_subnet_ids" {
  description = "Future private DB subnet IDs keyed by AZ slot."
  value       = { for az, subnet in aws_subnet.database : az => subnet.id }
}

output "alb_security_group_id" {
  description = "Future ALB SG ID."
  value       = aws_security_group.alb.id
}

output "application_security_group_id" {
  description = "Future application SG ID."
  value       = aws_security_group.application.id
}
