# All code pertaining graphical interface + input collection should go here
def intro():
    print('******WELCOME TO THE CREDIT CARD CALCULATOR******')
    print('To use this program, simply enter the information')
    print('that is requested. Next, a dollar result will be ')
    print('returned. This dollar result is how much you will')
    print('have to spend in order to earn enough rewards to ')
    print('offset the annual fee of a card.')
    print('*************************************************')


def collect_rr() -> float:
    rr = None
    while rr is None:  # This will loop until user inputs valid percentage
        try:
            user_rr = float(input('How much does your card earn (in percent; must be greater than 0)?: '))

            if user_rr > 0:
                rr = user_rr
            else:
                print('Sorry, that is not a valid rewards rate! Try again.')

            print()
        except ValueError:
            print('Sorry, that is not a valid rewards rate! Try again.')
    return rr


def collect_af() -> float:
    af = None
    while af is None:  # This will loop until user inputs a correct af
        try:
            user_af = float(input('How much is the annual fee on your card?: '))

            if user_af >= 0:  # This if/else statement is to ensure that user inputted af is positive
                af = user_af
            else:
                print('Sorry, that is not a valid annual fee! Try again.')

            print()

        except ValueError:  # This occurs bc user inputted invalid, non-numerical af
            print('Sorry, that is not a valid annual fee! Try again.')
    return af
