import inspect
import numpy as np
from typing import Union
from pprint import pprint
import numpy_financial as npf
from scipy.optimize import minimize_scalar


class BuyHold:
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
        :param vacancy_rate: either monthly amount or a percentage of the rent; default is 5%
        :param capex_rate: either a monthly amount or a percentage of the rent; default is 5%
        """
        # Error trapping
        assert interest_rate < 1

        # Handle input params
        self.rent = market_rent
        self.hoa = hoa
        self.loan_term = loan_term
        self.interest_rate = interest_rate
        self.capex = (capex_rate * self.rent if capex_rate < 1 else capex_rate)
        self.vacancy = (vacancy_rate * self.rent if vacancy_rate < 1 else vacancy_rate)
        self.property_mgt = (property_mgt * self.rent if property_mgt < 1 else property_mgt)
        self.profit = (desired_profit * self.rent if desired_profit < 1 else desired_profit)

        # Find optimal solution
        solution = minimize_scalar(self._objective, args=(down_payment, property_tax, insurance))

        # Calculate resultant values
        self.purchase_price = float(solution.x)
        self.down_payment = (self.purchase_price * down_payment if down_payment < 1 else down_payment)
        self.loan_amount = self.purchase_price - self.down_payment
        self.principle_interest = -1*npf.pmt(self.interest_rate/12, self.loan_term*12, self.loan_amount)
        self.tax = (self.purchase_price * property_tax if property_tax < 1 else property_tax)
        self.insurance = (self.purchase_price * insurance if insurance < 1 else insurance)
        self.mortgage = self.principle_interest + self.tax/12 + self.insurance/12

        self._formatter()

    def summary(self):
        summary = {
                'purchase_price': self.purchase_price,
                'market_rent': self.rent,
                'mortgage': {
                    'total': self.mortgage,
                    'principle_interest': {
                        'total': self.principle_interest,
                        'interest_rate': self.interest_rate,
                        'loan_term': self.loan_term,
                        'loan_amount': self.loan_amount,
                    },
                    'real_estate_tax': self.tax/12,
                    'hazard_insurance': self.insurance/12,
                },
                'home_owners_association': self.hoa,
                'property_management': self.property_mgt,
                'capex_allowance': self.capex,
                'vacancy_allowance': self.vacancy,
                'profit': self.profit
            }
        pprint(summary)

    def _objective(self, purchase_price: np.ndarray, down_payment, property_tax, insurance) -> float:
        # Principle and interest
        dp = (down_payment * purchase_price if down_payment < 1 else down_payment)
        pi = -1*npf.pmt(self.interest_rate/12, self.loan_term*12, purchase_price-dp)

        # Mortgage
        tax = (property_tax * purchase_price if property_tax < 1 else property_tax)
        ins = (insurance * purchase_price if insurance < 1 else insurance)
        mortgage = pi + tax/12 + ins/12

        expenses = mortgage + self.capex + self.vacancy + self.property_mgt + self.profit
        difference = self.rent - expenses
        return abs(difference)

    def _formatter(self):
        for attr_name, attr_value in inspect.getmembers(self):
            if not attr_name.startswith('_'):
                try:
                    setattr(self, attr_name, round(attr_value, 2))
                except TypeError:
                    continue
