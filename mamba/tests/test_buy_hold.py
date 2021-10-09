from mamba.calculator.buy_hold import BuyHold


def test_buy_hold_calculator():
    calc = BuyHold(
        market_rent=3381,
        desired_profit=100,
        interest_rate=0.04,
        hoa=(173/3),
        property_tax=3776.54,
        insurance=1170.23
    )
    calc.summary()
    assert True

