# This should pull everything together
from creditcard import CreditCard
from graphicalinterface import intro, collect_rr, collect_af

if __name__ == '__main__':
    intro()
    cc_name = input('Enter the name of your card: ')
    print()
    rr = collect_rr()
    af = collect_af()
    user_card = CreditCard(cc_name, rr, af)

    print(f'You told me that your {str(user_card)}')
    print(f'You have to spend a grand total of ${user_card.calc():.2f}')
    print(f'on your {cc_name} card in order to break even!')
    print()
    print('Thanks for using this program!')








