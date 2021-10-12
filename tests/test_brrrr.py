from mamba.calculator.brrrr import BRRRR


def test_brrrr_calculator():
    calc = BRRRR(
        arv=290000,
        rehab=10000,
        recap_rate=1,
        market_rent=1425,
        desired_profit=100,
        interest_rate=0.04,
        down_payment=0.20,
        hoa=237
    )
    calc.summary()
    assert isinstance(calc.purchase_price, float)
