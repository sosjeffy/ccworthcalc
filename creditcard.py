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

    def calc_be(self) -> float:
        '''Calculates break even spend on credit card'''
        spent = 0
        earned_per_dollar = 1 * (self.rr / 100)
        cost_to_go = self.af * -1

        while cost_to_go < 0:
            spent += earned_per_dollar
            cost_to_go += earned_per_dollar

        return spent

    def __repr__(self):
        return f'CreditCard({self.name}, {self.rr}, {self.af})'

    def __str__(self):
        return f'{self.name} earns {self.rr}% with an annual fee of ${self.af}'


assert str(CreditCard('SPG Biz', 3, 95)) == 'SPG Biz earns 3% with an annual fee of $95'

assert repr(CreditCard('', 10, 99483)) == "CreditCard(, 10, 99483)"
