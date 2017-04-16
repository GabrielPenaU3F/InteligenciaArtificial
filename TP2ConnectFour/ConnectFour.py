import sys

from Game import Game


def welcome():

    entry = raw_input('Welcome to Connect Four. Tip F to play first or S to play second. Tip Q to quit\n')
    if not ((entry == "S") or (entry == "F") or (entry == "Q")):
        print 'Invalid entry. Try again \n\n'
        welcome()

    elif (entry == "Q"): sys.exit()

    else:
        game = Game()
        game.start(entry)


welcome()