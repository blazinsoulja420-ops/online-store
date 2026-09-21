from dataclasses import dataclass
from enum import Enum

class Environment(str, Enum):
    DEVELOPMENT="development"
    PRODUCTION="production"

@dataclass(frozen=True)
class ProductOffer:
    sku: str
    supplier_ref: str
    price_cents: int

def may_spend_money(environment: Environment) -> bool:
    return False

def valid_offer(offer: ProductOffer) -> bool:
    return bool(offer.sku and offer.supplier_ref and offer.price_cents >= 0)
class OrderState(str, Enum):
    DRAFT="draft"
    READY="ready"
    BLOCKED="blocked"

def order_state(offer: ProductOffer) -> OrderState:
    return OrderState.READY if valid_offer(offer) else OrderState.BLOCKED

def live_provider_activation_allowed() -> bool:
    return False
