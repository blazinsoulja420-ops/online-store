# Product Requirements — Online Store

## Evidence classification
- VERIFIED: Repository exists and is standalone.
- REPORTED: No-inventory online store with management, monitoring, advertising, and Shopify/Supabase/Canva/Figma integration goals.
- UNKNOWN: Product niche, supplier network, pricing strategy, tax/legal configuration, payment processor, marketing budget, target market.

## Architecture boundary
Catalog/supplier abstraction → storefront → order lifecycle → fulfillment handoff → analytics/monitoring → marketing integrations.

## Phase 1 constraints
- Development/sandbox only.
- No paid ads, live purchases, production credentials, supplier commitments, or public auto-publishing.
- Credentials must be externalized.
- Supplier/product data requires provenance.

## Deliverables
Provider-neutral domain model, integration interfaces, sandbox storefront, mock supplier/order flows, tests, CI, docs, deployment plan with production activation separately gated.