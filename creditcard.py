# Code related to credit card information should go here
class CreditCard:
    def __init__(self, name: str, reward_rate: float = 0, annual_fee: int = 0):
        self.name = name
        self.rr = reward_rate
        self.af = annual_fee

    def name(self):
        return self.name

    def rr(self):
        return self.rr

    def af(self):
        return self.af

    def __repr__(self):
        return f'CreditCard({self.name}, {self.rr}, {self.af})'

    def __str__(self):
        return f'{self.name} earns {self.rr}% with an annual fee of {self.af}'


