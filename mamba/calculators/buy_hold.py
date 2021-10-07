from typing import Union


class BuyHoldCalculator:
    def __init__(self,
                 market_rent: int,
                 desired_profit: Union[int, float],
                 interest_rate: float,
                 loan_term: int = 30,
                 down_payment: Union[int, float] = 0.20,
                 property_tax: Union[int, float] = 0.0091,
                 insurance: Union[int, float] = 0.0025,
                 property_mgt: Union[int, float] = 0.10,
                 hoa: int = 0,
                 vacancy_rate: float = 0.05,
                 capex_rate: float = 0.05):
        """
        TODO add description

        :param market_rent: fair market monthly rent for the property
        :param desired_profit: monthly profit expressed as a dollar amount or percentage of rent
        :param interest_rate: expressed as a decimal; i.e. 4% APR would be 0.04
        :param loan_term: the length of the loan in number of years; default is 30
        :param down_payment: expressed as a dollar amount or percentage of the purchase price; default is 20%
        :param property_tax: expressed as a dollar amount (annually) or percentage purchase price; default is 0.91%
        :param insurance: expressed as a dollar amount (annually) or percentage of the purchase price; default is 0.25%
        :param property_mgt: expressed as a dollar amount (monthly) or percentage of the rent; default is 10%
        :param hoa: monthly payment to home owners association; default is 0
        :param vacancy_rate: percentage of the rent to be allocated for vacancies; default is 5%
        :param capex_rate: percentage of the rent to be allocated for capital expenditures; default is 5%
        """
        # Error trapping
        assert interest_rate < 1

        # Handle input params
        self.price = 1
        self.rent = market_rent
        self.profit = (desired_profit * self.rent if desired_profit < 1 else desired_profit)
        self.apr = interest_rate
        self.term = loan_term
        self.dp = (down_payment * self.price if down_payment < 1 else down_payment)






