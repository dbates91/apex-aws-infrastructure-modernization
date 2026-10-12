# DRAFT MODULE: Not referenced by any environment. Do not apply without budget approval.
locals {
  public_subnets = {
    a = { az = var.availability_zones[0], cidr = "10.0.0.0/24" }
    b = { az = var.availability_zones[1], cidr = "10.0.1.0/24" }
  }
  app_subnets = {
    a = { az = var.availability_zones[0], cidr = "10.0.10.0/24" }
    b = { az = var.availability_zones[1], cidr = "10.0.11.0/24" }
  }
  db_subnets = {
    a = { az = var.availability_zones[0], cidr = "10.0.20.0/24" }
    b = { az = var.availability_zones[1], cidr = "10.0.21.0/24" }
  }
  common_tags = merge(var.tags, {
    Project   = "Apex"
    ManagedBy = "Terraform"
  })
}

resource "aws_vpc" "this" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = merge(local.common_tags, { Name = "${var.project_name}-vpc" })
}

resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id
  tags   = merge(local.common_tags, { Name = "${var.project_name}-igw" })
}

resource "aws_subnet" "public" {
  for_each                = local.public_subnets
  vpc_id                  = aws_vpc.this.id
  availability_zone       = each.value.az
  cidr_block              = each.value.cidr
  map_public_ip_on_launch = false
  tags                    = merge(local.common_tags, { Name = "${var.project_name}-public-${each.key}", Tier = "public" })
}

resource "aws_subnet" "application" {
  for_each                = local.app_subnets
  vpc_id                  = aws_vpc.this.id
  availability_zone       = each.value.az
  cidr_block              = each.value.cidr
  map_public_ip_on_launch = false
  tags                    = merge(local.common_tags, { Name = "${var.project_name}-app-${each.key}", Tier = "application" })
}

resource "aws_subnet" "database" {
  for_each                = local.db_subnets
  vpc_id                  = aws_vpc.this.id
  availability_zone       = each.value.az
  cidr_block              = each.value.cidr
  map_public_ip_on_launch = false
  tags                    = merge(local.common_tags, { Name = "${var.project_name}-db-${each.key}", Tier = "database" })
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.this.id
  tags   = merge(local.common_tags, { Name = "${var.project_name}-public-rt" })
}

resource "aws_route" "public_default" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.this.id
}

resource "aws_route_table_association" "public" {
  for_each       = aws_subnet.public
  route_table_id = aws_route_table.public.id
  subnet_id      = each.value.id
}

# Private subnet route tables deliberately have no 0.0.0.0/0 route.
# NAT gateways/endpoints are omitted pending budget and outbound policy approval.
resource "aws_route_table" "application" {
  for_each = local.app_subnets
  vpc_id   = aws_vpc.this.id
  tags     = merge(local.common_tags, { Name = "${var.project_name}-app-rt-${each.key}" })
}

resource "aws_route_table_association" "application" {
  for_each       = aws_subnet.application
  route_table_id = aws_route_table.application[each.key].id
  subnet_id      = each.value.id
}

resource "aws_route_table" "database" {
  for_each = local.db_subnets
  vpc_id   = aws_vpc.this.id
  tags     = merge(local.common_tags, { Name = "${var.project_name}-db-rt-${each.key}" })
}

resource "aws_route_table_association" "database" {
  for_each       = aws_subnet.database
  route_table_id = aws_route_table.database[each.key].id
  subnet_id      = each.value.id
}

resource "aws_security_group" "alb" {
  name_prefix            = "${var.project_name}-alb-"
  description            = "Future ALB HTTPS ingress and scoped application egress"
  vpc_id                 = aws_vpc.this.id
  revoke_rules_on_delete = true
  tags                   = merge(local.common_tags, { Name = "${var.project_name}-alb-sg" })
}

resource "aws_security_group" "application" {
  name_prefix            = "${var.project_name}-app-"
  description            = "Future private application instances with restricted ALB ingress"
  vpc_id                 = aws_vpc.this.id
  revoke_rules_on_delete = true
  tags                   = merge(local.common_tags, { Name = "${var.project_name}-app-sg" })
}

resource "aws_vpc_security_group_ingress_rule" "alb_https" {
  security_group_id = aws_security_group.alb.id
  description       = "HTTPS client access to a future public ALB"
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 443
  to_port           = 443
  ip_protocol       = "tcp"
}

resource "aws_vpc_security_group_egress_rule" "alb_to_app" {
  security_group_id            = aws_security_group.alb.id
  description                  = "ALB to app target"
  referenced_security_group_id = aws_security_group.application.id
  from_port                    = var.app_port
  to_port                      = var.app_port
  ip_protocol                  = "tcp"
}

resource "aws_vpc_security_group_ingress_rule" "app_from_alb" {
  security_group_id            = aws_security_group.application.id
  description                  = "App port from future ALB only"
  referenced_security_group_id = aws_security_group.alb.id
  from_port                    = var.app_port
  to_port                      = var.app_port
  ip_protocol                  = "tcp"
}

# No application egress is authorized yet. Systems Manager requires a planned
# outbound connection via approved NAT or VPC endpoints and appropriate SG rules.
