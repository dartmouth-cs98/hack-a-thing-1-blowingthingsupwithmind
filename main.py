"""
Main script

Author:         Josh Kerber & Brophy Tyree
Date:           01/10/2018
Project:        CS98 Hack-a-thing 1
"""

from packages.Emotiv import Emotiv
from packages.Util import *
import json
import os

# instantiate Emotiv connection
EMOTIV = Emotiv()

# store training status
TRAINED_PUSH = False
TRAINED_NEUTRAL = False

# help message
USAGE = '''COMMANDS: 'train neutral' 'train push' 'test' 'exit' '--help' '''

def run():
    """run Emotiv mental command session"""
    global TRAINED_NEUTRAL, TRAINED_PUSH
    if not EMOTIV.initialize():
        inform('unable to initialize emotiv connection')
        return
    inform('emotiv initialized', clear=True)
    print(USAGE)

    # recieve input indefinitely
    while True:
        cmd = input('\n\t==> command : ')
        print()

        # train mental commands
        if cmd == 'train neutral':
            TRAINED_NEUTRAL = EMOTIV.train('neutral')
        elif cmd == 'train push':
            if not TRAINED_NEUTRAL:
                print('you must train neutral command first')
                continue
            TRAINED_PUSH = EMOTIV.train('push')

        # test mental commands
        elif cmd == 'test':
            if not TRAINED_PUSH:
                print('you must train push command first')
                continue
            EMOTIV.test()

        # system commands
        elif cmd == 'exit':
            break
        elif cmd == '--help':
            print(USAGE)
        else:
            print('command not found')
            print('enter \'--help\' for commands', end='\n\n')

    # disconnect from web socket
    EMOTIV.disconnect()
    inform('emotiv disconnected', clear=True)
    print('GOODBYE', end='\n\n')

def main():
    """run program"""
    EMOTIV.connect(run)

if __name__ == "__main__":
    main()
