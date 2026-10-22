# APX-001 — Read-only Repository & Terraform Safety Audit

**Status:** Not Started · **Estimated active time:** 25–40 minutes · **AWS cost:** $0 · **Deployment:** prohibited for this ticket

## Scenario

You have joined a cloud operations team supporting Apex. The previous engineer left a GitHub repository with a Terraform networking module and a development root. Before the team grants deployment access, you must prove which files *could* create infrastructure, which files are safe to inspect, and what remains unverified.

## Prerequisites and concepts

- Git repository = source history and desired configurations, not the AWS account's actual state.
- A **Terraform provider** allows Terraform to communicate with a target API. Declaring a provider does not itself create a VPC.
- A **Terraform resource** block represents a managed infrastructure object *when included in an applied root configuration*.
- A **Terraform module** groups configuration; a draft module not called by a root is not deployed by that root.
- Terraform state is a sensitive mapping between configuration and managed objects. Do not assume cloud resources exist because .tf source exists.

## Scope

Read-only inspections of:
- README.md
- terraform/environments/dev/versions.tf
- terraform/environments/dev/README.md
- terraform/modules/networking/README.md
- PROJECT_TRACKER.md and COST_MANAGEMENT.md

No AWS deployments, terraform apply or destroy, repository rewrites, credentials, or account details in public notes.

## Workflow and acceptance criteria

1. **Locate** the current local repository (or clone to a clean local directory if needed).
2. **Inspect** the dev Terraform root and networking module without editing or applying them.
3. **Explain** in your own words why the dev root does not deploy a VPC and how the networking module would become active.
4. **Identify** the first three blockers to safe deployment (account/budget audit, regional/network/SSM design, implementation/teardown approval).
5. **Validate** a local command and interpret its actual output (instructor selects command based on installed tools).
6. **Troubleshooting challenge:** a teammate says “I see aws_vpc in a .tf file, so the VPC already exists.” Correct this conclusion and describe how you'd verify reality.
7. **Document** no-cost evidence and 60–90 second interview explanation, without secrets.

## Mastery questions (ask one at a time)

- What is the difference between declaring a Terraform provider and creating an aws_vpc resource?
- Why does the safe dev root not deploy the draft networking module?
- What would you inspect before anyone executes Terraform apply?
- What kinds of evidence prove a VPC actually exists, as opposed to Terraform syntax being valid?

## Instructor pacing

Teach only the *next step* after evaluating the previous user output. Start by identifying which machine holds the local clone and checking the working directory and Git context. Do not disclose a full command solution list before the user attempts the lab.

## GitHub deliverable

A concise dated, sanitized audit note with inspected paths, what each file does, actual local verification command/output, hazards, blockers and next action. Keep this ticket marked **Not Started** until user produces evidence.
