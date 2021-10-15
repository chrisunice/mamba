from .buy_hold import BuyHold


class BRRRR(BuyHold):
    def __init__(self, arv: int, rehab: int, recap_rate: float = 1, refi_ltv: float = 0.80, **kwargs):
        """
        Calculator to determine the purchase price of a property using the BRRRR method

        :param arv: after repair value of the property
        :param rehab: cost to repair the property
        :param recap_rate: percentage of capital to recover from the refinance; default is 1 (100%)
        :param refi_ltv: percentage of the `arv` that a bank will refinance; default is 0.80 (80%)
        :param kwargs: parameters to pass to parent class
            - market_rent
            - desired_profit
            - interest_rate
            - loan_term
            - down_payment
            - property_tax
            - insurance
            - property_mgt
            - hoa
            - vacancy_rate
            - capex_rate
        """
        super().__init__(**kwargs)

        # Handle input params
        self.arv = arv
        self.rehab = rehab
        self.recap_rate = recap_rate
        self.refi_ltv = refi_ltv

        # Purchase price must satisfy both traditional and BRRRR methods
        self.capital_out = self.arv * self.refi_ltv
        self.brrrr_price = self.capital_out / self.recap_rate - self.rehab
        self.traditional_price = self.purchase_price
        self.purchase_price = (self.brrrr_price if self.brrrr_price < self.traditional_price else self.traditional_price)

        self.capital_in = self.purchase_price + self.rehab
        self.cocr = self.get_cash_on_cash_roi(self.profit, self.capital_in-self.capital_out)

    def summary(self):
        spacing = ' '*30
        line = '-'*40
        prefix = f"\n\tBRRRR Method" \
                 f"\n\t{line}"

        limit_factor = ('MARKET VALUE' if self.brrrr_price == self.purchase_price else 'MARKET RENT')
        suffix = f"\n\t{line}" \
                 f"\n\t{'Constrained by the '+limit_factor+' method'}" \
                 f"\n\t{'Capital Invested:'+spacing:.30s}$ {self.capital_in:,.2f}" \
                 f"\n\t{'  Rehab Cost:'+spacing:.30s}$ {self.rehab:,.2f}" \
                 f"\n\t{'Capital Recovered:'+spacing:.30s}$ {self.capital_out:,.2f}" \
                 f"\n\t{'  Refinance LTV:'+spacing:.30s} {self.refi_ltv*100:.2f}%" \
                 f"\n\t{'Capital Lost:'+spacing:.30s}$ {self.capital_in-self.capital_out:,.2f}" \
                 f"\n\t{'  Recapture Rate:' + spacing:.30s} {self.recap_rate*100:.2f}%"
        print(prefix + self._summary + suffix)
