from online_store_foundation import Environment, ProductOffer, may_spend_money, valid_offer

def test_phase_one_never_spends_money():
    assert may_spend_money(Environment.DEVELOPMENT) is False
    assert may_spend_money(Environment.PRODUCTION) is False

def test_offer_requires_provenance_reference():
    assert valid_offer(ProductOffer("sku1","supplier:item1",1000))
    assert not valid_offer(ProductOffer("sku1","",1000))
def test_order_validation_and_live_activation_gate():
    from online_store_foundation import OrderState, ProductOffer, order_state, live_provider_activation_allowed
    assert order_state(ProductOffer("sku","supplier:item",500))==OrderState.READY
    assert order_state(ProductOffer("sku","",500))==OrderState.BLOCKED
    assert live_provider_activation_allowed() is False
def test_draft_order_is_provider_neutral_and_fail_closed():
    from online_store_foundation import DraftOrder, OrderState, ProductOffer, validate_draft_order
    offer=ProductOffer("sku","supplier:item",500)
    assert validate_draft_order(DraftOrder(offer,1))==OrderState.READY
    assert validate_draft_order(DraftOrder(offer,0))==OrderState.BLOCKED


def test_offer_rejects_blank_ids_and_noninteger_price():
    assert not valid_offer(ProductOffer("  ", "supplier:item", 500))
    assert not valid_offer(ProductOffer("sku", "  ", 500))
    assert not valid_offer(ProductOffer("sku", "supplier:item", True))
    assert not valid_offer(ProductOffer("sku", "supplier:item", 12.5))


def test_draft_order_requires_positive_integer_quantity():
    from math import nan
    from online_store_foundation import DraftOrder, OrderState, validate_draft_order
    offer = ProductOffer("sku", "supplier:item", 500)
    for quantity in (-1, 0, True, 1.5, nan, "2"):
        assert validate_draft_order(DraftOrder(offer, quantity)) == OrderState.BLOCKED
