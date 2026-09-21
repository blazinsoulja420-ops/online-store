from online_store_foundation import Environment, ProductOffer, may_spend_money, valid_offer

def test_phase_one_never_spends_money():
    assert may_spend_money(Environment.DEVELOPMENT) is False
    assert may_spend_money(Environment.PRODUCTION) is False

def test_offer_requires_provenance_reference():
    assert valid_offer(ProductOffer("sku1","supplier:item1",1000))
    assert not valid_offer(ProductOffer("sku1","",1000))
