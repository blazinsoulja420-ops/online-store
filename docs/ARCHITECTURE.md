# Phase 1 Architecture

## Purpose
Turn the recovered product requirements into a minimal, testable engineering foundation without expanding scope.

## Architecture rules
- Keep this repository standalone.
- Reference shared AI behavior and UARS capabilities through explicit interfaces only.
- Separate domain logic from provider/vendor integrations.
- Keep production credentials, paid services, deployment, and destructive operations outside this phase.
- Preserve auditable state transitions and deterministic business/safety rules.

## Layering
1. Domain models and invariants
2. Application/use-case services
3. Provider/integration interfaces
4. Infrastructure adapters
5. API/UI boundary
6. Tests and CI

## Phase 1 implementation target
Build the smallest runnable/dev-test foundation that can prove the known requirements without inventing unresolved features.

## Exit criteria
- documented domain model
- explicit acceptance criteria
- test scaffolding
- CI workflow
- minimal runnable entry point or service skeleton
- remaining UNKNOWN/BLOCKED items documented
