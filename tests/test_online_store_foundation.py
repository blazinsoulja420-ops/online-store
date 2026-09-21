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
