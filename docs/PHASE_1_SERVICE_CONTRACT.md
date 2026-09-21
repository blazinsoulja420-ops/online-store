# Phase 1 Service Contract

Status: IMPLEMENTATION BOUNDARY

This repository's Phase 1 application workflow is intentionally local, deterministic, and provider-neutral.

## Contract

- Domain rules remain independent from infrastructure providers.
- Persistence is represented through explicit interfaces before any database is selected.
- External systems are referenced through adapters/contracts rather than copied into this repository.
- Tests must exercise domain and application behavior without production credentials or network access.
- Production activation, deployment, paid actions, destructive operations, and live credentials remain outside Phase 1 authority.

## Current acceptance boundary

The existing application workflow and its tests are the authoritative executable proof for this phase. The next implementation layer may add in-memory repository interfaces and API-shaped request/response contracts, but must not silently select a production provider or weaken existing safety boundaries.
