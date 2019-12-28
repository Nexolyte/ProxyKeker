from colorama import init
import sys
import os

import check
import scrape
from utils import *

sys.stdout.write("\x1b]2;ProxyKeker by Nexolyte\x07")

os.system('cls')

init()

class proxykeker():
    def __init__(self):
        self.main()

    def main(self):
        print(red + '''
  _____                     _  __    _             
 |  __ \\                   | |/ /   | |            
 | |__) | __ _____  ___   _| ' / ___| | _____ _ __ 
 |  ___/ '__/ _ \\ \\/ / | | |  < / _ \\ |/ / _ \\ '__|
 | |   | | | (_) >  <| |_| | . \\  __/   <  __/ |   
 |_|   |_|  \\___/_/\\_\\\\__, |_|\\_\\___|_|\\_\\___|_|   
                       __/ |                       
                      |___/                        \n''')
        print(blue + 'by Nexolyte\n')
        m = get('Main Menu\n' +\
                red + '[' + blue + '1' + red + '] - ' + white + 'Scrape\n' +\
                red + '[' + blue + '2' + red + '] - ' + white + 'Check\n' +\
                red + '[' + blue + 'e' + red + '] - ' + white + 'Exit\n')

        if m == '1':
            os.system('cls')
            scrape.scrape()
        elif m == '2':
            os.system('cls')
            check.check()
        elif m == 'e':
            os.system('cls')
            sys.exit(1)
        else:
            os.system('cls')
            error('Input not recognised. Please retype and try again.')
            self.main()

if __name__ == '__main__':
    proxykeker()
