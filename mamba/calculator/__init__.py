import numpy as np


class BaseCalculator:
    def __init__(self):
        self.purchase_price = 0
        self.down_payment = 0
        self.rent = 0
        self.mortgage = 0
        self.principle_interest = 0
        self.interest_rate = 0
        self.loan_term = 0
        self.loan_amount = 0
        self.tax = 0
        self.insurance = 0
        self.hoa = 0
        self.property_mgt = 0
        self.capex = 0
        self.vacancy = 0
        self.profit = 0
        self.cocr = 0

    @property
    def _summary(self):
        spacing = ' '*30
        return f"\n\t{'Purchase Price:'+spacing:.30s}$ {self.purchase_price:,.2f}" \
               f"\n\t{'Down Payment:'+spacing:.30s}$ {self.down_payment:,.2f}" \
               f"\n\t{'Market Rent:'+spacing:.30s}$ {self.rent:,.2f}" \
               f"\n" \
               f"\n\t{'Mortgage:'+spacing:.30s}$ {self.mortgage:,.2f}" \
               f"\n\t{'  Principle & Interest:'+spacing:.30s}$ {self.principle_interest:,.2f}" \
               f"\n\t{'    Interest Rate:'+spacing:.30s} {self.interest_rate*100:.2f}%" \
               f"\n\t{'    Loan Term:'+spacing:.30s} {self.loan_term:.0f}" \
               f"\n\t{'    Loan Amount:'+spacing:.30s}$ {self.loan_amount:,.2f}" \
               f"\n\t{'  Real Estate Tax:'+spacing:.30s}$ {self.tax/12:,.2f}" \
               f"\n\t{'  Hazard Insurance:'+spacing:.30s}$ {self.insurance/12:,.2f}" \
               f"\n" \
               f"\n\t{'HOA:'+spacing:.30s}$ {self.hoa:,.2f}" \
               f"\n\t{'Property Management:'+spacing:.30s}$ {self.property_mgt:,.2f}" \
               f"\n\t{'Capital Expenditures:'+spacing:.30s}$ {self.capex:,.2f}" \
               f"\n\t{'Vacancy:'+spacing:.30s}$ {self.vacancy:,.2f}" \
               f"\n" \
               f"\n\t{'Profit:'+spacing:.30s}$ {self.profit:,.2f}" \
               f"\n\t{'Cash-on-cash Return'+spacing:.30s} {self.cocr*100:.2f}%"

    @staticmethod
    def get_roi():
        pass

    @staticmethod
    def get_cash_on_cash_roi(monthly_cash_flow, capital_invested):
        capital_invested = (0 if capital_invested < 0 else capital_invested)
        try:
            return (monthly_cash_flow * 12)/capital_invested
        except ZeroDivisionError:
            return np.inf
