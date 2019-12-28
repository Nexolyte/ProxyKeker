import sys
import os
import requests
import time
import threading

import proxykeker
from utils import *

screenlock = threading.Semaphore(value=1)

class check():
    def __init__(self):
        self.proxies_type = ''
        self.proxies_file = ''
        self.test_url = 'https://www.google.com/robots.txt'
        self.threads = 50
        self.timeout = 5

        self.dead = 0
        self.alive = 0
        self.to_check = []

        self.proxy_file()

    def proxy_file(self):
        os.system('cls')

        print(red + '''
  _____                     _  __    _             
 |  __ \\                   | |/ /   | |            
 | |__) | __ _____  ___   _| ' / ___| | _____ _ __ 
 |  ___/ '__/ _ \\ \\/ / | | |  < / _ \\ |/ / _ \\ '__|
 | |   | | | (_) >  <| |_| | . \\  __/   <  __/ |   
 |_|   |_|  \\___/_/\\_\\\\__, |_|\\_\\___|_|\\_\\___|_|   
                       __/ |                       
                      |___/                        \n''')

        print(self.proxies_file)
        self.proxies_file = get('Enter the name of the file with the proxies: ')
        if not self.proxies_file:
            os.system('cls')
            error('Specified file does not exist. Please try again.')
            self.proxy_file()
        else:
            self.proxy_type()

    def proxy_type(self):
        os.system('cls')

        print(red + '''
  _____                     _  __    _             
 |  __ \\                   | |/ /   | |            
 | |__) | __ _____  ___   _| ' / ___| | _____ _ __ 
 |  ___/ '__/ _ \\ \\/ / | | |  < / _ \\ |/ / _ \\ '__|
 | |   | | | (_) >  <| |_| | . \\  __/   <  __/ |   
 |_|   |_|  \\___/_/\\_\\\\__, |_|\\_\\___|_|\\_\\___|_|   
                       __/ |                       
                      |___/                        \n''')

        m = get('Please specify the type of the proxies\n' +\
                red + '[' + blue + '1' + red + '] - ' + white + 'HTTP/S\n' +\
                red + '[' + blue + '2' + red + '] - ' + white + 'SOCKS4\n' +\
                red + '[' + blue + '3' + red + '] - ' + white + 'SOCKS5\n')

        if m == '1':
            self.proxies_type = 'http'
            self.proxy_thread()
        elif m == '2':
            self.proxies_type = 'socks4'
            self.proxy_thread()
        elif m == '3':
            self.proxies_type = 'socks5'
            self.proxy_thread()
        else:
            os.system('cls')
            error('ERROR: Input not recognised. Please retype and try again.')
            self.proxy_type()
    
    def proxy_thread(self):
        os.system('cls')

        print(red + '''
  _____                     _  __    _             
 |  __ \\                   | |/ /   | |            
 | |__) | __ _____  ___   _| ' / ___| | _____ _ __ 
 |  ___/ '__/ _ \\ \\/ / | | |  < / _ \\ |/ / _ \\ '__|
 | |   | | | (_) >  <| |_| | . \\  __/   <  __/ |   
 |_|   |_|  \\___/_/\\_\\\\__, |_|\\_\\___|_|\\_\\___|_|   
                       __/ |                       
                      |___/                        \n''')

        m = get('Please enter the number of threads\n')

        self.proxy_threads = m
        
        self.proxy_timeout()
    
    def proxy_timeout(self):
        os.system('cls')

        print(red + '''
  _____                     _  __    _             
 |  __ \\                   | |/ /   | |            
 | |__) | __ _____  ___   _| ' / ___| | _____ _ __ 
 |  ___/ '__/ _ \\ \\/ / | | |  < / _ \\ |/ / _ \\ '__|
 | |   | | | (_) >  <| |_| | . \\  __/   <  __/ |   
 |_|   |_|  \\___/_/\\_\\\\__, |_|\\_\\___|_|\\_\\___|_|   
                       __/ |                       
                      |___/                        \n''')

        m = get('Please enter the timeout (in seconds)\n')

        self.timeout = m
        
        self.proxy_check()

    def proxy_check(self):
        os.system('cls')

        print(red + '''
  _____                     _  __    _             
 |  __ \\                   | |/ /   | |            
 | |__) | __ _____  ___   _| ' / ___| | _____ _ __ 
 |  ___/ '__/ _ \\ \\/ / | | |  < / _ \\ |/ / _ \\ '__|
 | |   | | | (_) >  <| |_| | . \\  __/   <  __/ |   
 |_|   |_|  \\___/_/\\_\\\\__, |_|\\_\\___|_|\\_\\___|_|   
                       __/ |                       
                      |___/                        \n''')

        checking = True

        with open(self.proxies_file, 'r') as f:
            self.proxy_count = sum(1 for proxy in open(self.proxies_file))
            action('Loaded {} proxies.'.format(self.proxy_count))
            
            for proxy in f:
                self.to_check.append(proxy.strip())

        action('Starting {} threads.'.format(self.proxy_threads))

        threads = []
        for i in range(self.threads):
            threads.append(threading.Thread(target=self.check_proxies))
            threads[i].setDaemon(True)
            threads[i].start()
        
        for thread in threads:
            thread.join()

        os.system('cls')
        print('{} alive | {} dead'.format(self.alive, self.dead))
        proxykeker.proxykeker()

    def check_proxies(self):
        while len(self.to_check) > 0:
            proxy = self.to_check[0]
            self.to_check.pop(0)

            screenlock.acquire()
            print('{} left | {} alive | {} dead'.format(len(self.to_check), self.alive, self.dead), end='\r')
            screenlock.release()

            try:
                requests.get(self.test_url, proxies={'http': self.proxies_type + '://' + proxy + '/'}, timeout=int(self.timeout))
            except:
                self.dead = self.dead + 1
            else:
                save_to_file('checked_{}.txt'.format(self.proxies_type), proxy)
                self.alive = self.alive + 1
    
        if len(threading.enumerate()) - 1 == 0:
            os.system('cls')
            print('{} alive | {} dead'.format(self.alive, self.dead))
            proxykeker.proxykeker()