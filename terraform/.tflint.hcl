# Terraform language linting. AWS-specific plugin rules can be enabled later
# after provider/module code and cost/security exceptions are reviewed.
plugin "terraform" {
  enabled = true
  preset  = "recommended"
}
