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
    while True:
        try:
            rr = float(input('How much does your card earn (in percent)?: '))
            print()
            break
        except ValueError:
            print('Sorry, that is not a valid rewards rate! Try again.')
            print()
            rr = collect_rr()
            print()
    return rr

def collect_af() -> float:
    while True:
        try:
            af = float(input('How much is the annual fee on your card?: '))
            print()
            break
        except ValueError:
            print('Sorry, that is not a valid annual fee! Try again.')
            print()
            af = collect_af()
            print()
    return af