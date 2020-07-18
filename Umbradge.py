# -*- coding: utf-8 -*-

from ascii import headers
import os, sys, random
import socket
import optparse
from scapy.all import *
from scapy.layers.inet import IP, UDP, TCP, ICMP
import subprocess
from tools.ddos import *
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import numpy as np
from tools.Osint.Instagram.searchInstagram import searchInstagram
from tools.Osint.Twitter.searchTwitter import searchTwitter
from tools.Osint.usernameLookup.searchUsername import searchUserName
from tools.Osint.ipLookup.ipLookUp import ipFinder
from tools.Osint.EmployeeLookup.searchEmployee import employee_lookup
from tools.Osint.PhoneLookUp.phoneLookUp import phoneLookup
from tools.Osint.Traceroute.traceroute import traceroute
from tools.Sniffing.ftp.ftpCredentials import ftp
from tools.Sniffing.packet.packet import packet
from tools.bufferOverflow.win32 import win32
from tools.donation import donation
from tools.SocialEngineering.Instagram.insta import createAccount
from tools.ShellCode.local import local
from tools.ShellCode.web import web
from tools.ShellCode.reverse import reverse
from tools.anonymize.macAdress import macAdress
from tools.anonymize.httpProxy import httpProxy
from tools.anonymize.httpsProxy import httpsProxy

if not os.geteuid() == 0:
    sys.exit("\nOnly root can run this script\n")

class colors:
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    WHITE = '\033[37m'
    RANDOM = random.choice([BLUE, GREEN, WHITE])

prompt = colors.WHITE + 'Umbradge: ~ $ '

def menu():
    print(headers())
    tools = colors.RED + '''
    {1}-- Social Engineering
    {2}-- ShellCode
    {3}-- Sniffing & Spoofing
    {4}-- Buffer Overflow
    {5}-- Web Hacking
    {6}-- Post Exploitation
    {7}-- BruteForce
    {8}-- Osint
    {9}-- Wireless Attacks
    {10}-- Anonymize
    {99}-- Exit
    {100}-- Donation
    '''
    print(tools)

    choice = int(input(prompt))
    if choice == 1:
        SocialEngineering()
    elif choice == 2:
        ShellCode()
    elif choice == 3:
        SniffingSpoofing()
    elif choice == 4:
        bufferOverflow()
    elif choice == 5:
        WebHacking()
    elif choice == 6:
        PostExploitation()
    elif choice == 7:
        BruteForce()
    elif choice == 8:
        Osint()
    elif choice == 9:
        WirelessAttack()
    elif choice == 10:
        Anonymize()
    elif choice == 99:
        exit()
    elif choice == 100:
        Donation()

def SocialEngineering():
    logo = colors.RANDOM + '''
     ____             _       _   _____             _                      _
    / ___|  ___   ___(_) __ _| | | ____|_ __   __ _(_)_ __   ___  ___ _ __(_)_ __   __ _
    \___ \ / _ \ / __| |/ _` | | |  _| | '_ \ / _` | | '_ \ / _ \/ _ \ '__| | '_ \ / _` |
     ___) | (_) | (__| | (_| | | | |___| | | | (_| | | | | |  __/  __/ |  | | | | | (_| |
    |____/ \___/ \___|_|\__,_|_| |_____|_| |_|\__, |_|_| |_|\___|\___|_|  |_|_| |_|\__, |
                                              |___/                                |___/
    '''
    print(logo)
    tools = colors.RED + '''
    {1}-- Phishing
    {2}-- Spear-phishing
    {3}-- Profile Generator
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))

    if choice == 3:
        logo = colors.RANDOM + '''
         ____             __ _ _         ____                           _
        |  _ \ _ __ ___  / _(_) | ___   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
        | |_) | '__/ _ \| |_| | |/ _ \ | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
        |  __/| | | (_) |  _| | |  __/ | |_| |  __/ | | |  __/ | | (_| | || (_) | |
        |_|   |_|  \___/|_| |_|_|\___|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|
        '''
        print(logo)
        tools = colors.RED = '''
        {1}-- Facebook
        {2}-- Instagram
        {3}-- Twitter
        {4}-- LinkedIn
        {5}-- Gmail
        {6}-- OutLook
        {7}-- ProtonMail
        {99}-- Exit
        '''
        print(tools)
        choice = int(input(prompt))
        if choice == 1:
            createAccount()
        elif choice == 99:
            menu()
    elif choice == 99:
        menu()

def ShellCode():
    logo = colors.RANDOM + '''
     ____  _          _ _    ____          _
    / ___|| |__   ___| | |  / ___|___   __| | ___
    \___ \| '_ \ / _ \ | | | |   / _ \ / _` |/ _ \\
     ___) | | | |  __/ | | | |__| (_) | (_| |  __/
    |____/|_| |_|\___|_|_|  \____\___/ \__,_|\___|
    '''

    print(logo)
    tools = colors.RED + '''
    {1}-- /bin/sh
    {2}-- Web
    {3}-- Reverse
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))
    if choice == 1:
        local()

    elif choice == 2:
        web()

    elif choice == 3:
        reverse()

    elif choice == 99:
        menu()

def SniffingSpoofing():
    logo = colors.RANDOM + '''
     ____        _  __  __ _                ___     ____                     __ _
    / ___| _ __ (_)/ _|/ _(_)_ __   __ _   ( _ )   / ___| _ __   ___   ___  / _(_)_ __   __ _
    \___ \| '_ \| | |_| |_| | '_ \ / _` |  / _ \/\ \___ \| '_ \ / _ \ / _ \| |_| | '_ \ / _` |
     ___) | | | | |  _|  _| | | | | (_| | | (_>  <  ___) | |_) | (_) | (_) |  _| | | | | (_| |
    |____/|_| |_|_|_| |_| |_|_| |_|\__, |  \___/\/ |____/| .__/ \___/ \___/|_| |_|_| |_|\__, |
                                   |___/                 |_|                            |___/
    '''
    print(logo)
    tools = colors.RED + '''
    {1}-- Sniffing
    {2}-- Spoofing
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))

    if choice == 1:
        logo = colors.RANDOM + '''
         ____        _  __  __ _
        / ___| _ __ (_)/ _|/ _(_)_ __   __ _
        \___ \| '_ \| | |_| |_| | '_ \ / _` |
         ___) | | | | |  _|  _| | | | | (_| |
        |____/|_| |_|_|_| |_| |_|_| |_|\__, |
                                       |___/
        '''
        print(logo)
        tools = colors.RED + '''
        {1}-- FTP Credentials
        {2}-- Packet Sniffer
        {3}-- Router Configuration
        {4}-- DNS Traffic
        {5}-- TCP/IP Sniffing
        {99}-- Exit
        '''

        print(tools)
        choice = int(input(prompt))
        if choice == 1:
            ftp()

        if choice == 2:
            packet()

        elif choice == 99:
            menu()

    elif choice == 2:
        logo = colors.RANDOM + '''
         ____                     __ _
        / ___| _ __   ___   ___  / _(_)_ __   __ _
        \___ \| '_ \ / _ \ / _ \| |_| | '_ \ / _` |
         ___) | |_) | (_) | (_) |  _| | | | | (_| |
        |____/| .__/ \___/ \___/|_| |_|_| |_|\__, |
              |_|                            |___/
                '''
        print(logo)
        tools = colors.RED + '''
        {1}-- MAC Flooding
        {2}-- DHCP Attacks
        {3}-- ARP Poisoning
        {4}-- VoIP / SIP Spoofing
        {99}-- Exit
        '''
        print(tools)
        choice = int(input(prompt))

        if choice == 99:
            menu()
            
    if choice == 99:
        menu()

def bufferOverflow():
    logo = colors.RANDOM + '''
     ____         __  __              ___                  __ _
    | __ ) _   _ / _|/ _| ___ _ __   / _ \__   _____ _ __ / _| | _____      __
    |  _ \| | | | |_| |_ / _ \ '__| | | | \ \ / / _ \ '__| |_| |/ _ \ \ /\ / /
    | |_) | |_| |  _|  _|  __/ |    | |_| |\ V /  __/ |  |  _| | (_) \ V  V /
    |____/ \__,_|_| |_|  \___|_|     \___/  \_/ \___|_|  |_| |_|\___/ \_/\_/
    '''
    print(logo)
    tools = colors.RED + '''
    {1}-- Windows 32bits
    {2}-- Linux 32bits
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))

    if choice == 1:
        win32()
    elif choice == 99:
        menu()

def WebHacking():
    logo = colors.RANDOM + '''
    __        __   _       _   _            _    _
    \ \      / /__| |__   | | | | __ _  ___| | _(_)_ __   __ _
     \ \ /\ / / _ \ '_ \  | |_| |/ _` |/ __| |/ / | '_ \ / _` |
      \ V  V /  __/ |_) | |  _  | (_| | (__|   <| | | | | (_| |
       \_/\_/ \___|_.__/  |_| |_|\__,_|\___|_|\_\_|_| |_|\__, |
                                                         |___/
    '''
    print(logo)
    tools = colors.RED + '''
    {1}-- XSS Scanner & Exploit
    {2}-- SQLi Scanner & Exploit
    {3}-- LFI / RFI Scanner
    {3}-- Enumeration
    {4}-- WordPress Scanner & Bruteforcer
    {5}-- DoS Attacks
    {6}-- DDoS Attacks
    {7}-- CSRF Scanner & Exploit
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))

    if choice == 1:
        print('Not Ready For The Moment')
    elif choice == 99:
        menu()

def PostExploitation():
    logo = colors.RANDOM + '''
     ____           _     _____            _       _ _        _   _
    |  _ \ ___  ___| |_  | ____|_  ___ __ | | ___ (_) |_ __ _| |_(_) ___  _ __
    | |_) / _ \/ __| __| |  _| \ \/ / '_ \| |/ _ \| | __/ _` | __| |/ _ \| '_ \\
    |  __/ (_) \__ \ |_  | |___ >  <| |_) | | (_) | | || (_| | |_| | (_) | | | |
    |_|   \___/|___/\__| |_____/_/\_\ .__/|_|\___/|_|\__\__,_|\__|_|\___/|_| |_|
                                    |_|
    '''
    print(logo)
    tools = colors.RED + '''
    {1}-- Privilege Escalation
    {2}-- Process Migration
    {3}-- Dump Password's Hash
    {4}-- Erase Logs
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))
    if choice == 1:
        print('Not Ready For The Moment')
    elif choice == 99:
        menu()

def BruteForce():
    logo = colors.RANDOM + '''
     ____             _       _____
    | __ ) _ __ _   _| |_ ___|  ___|__  _ __ ___ ___
    |  _ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ \
    | |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/
    |____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|
    '''

    print(logo)
    tools = colors.RED + '''
    {1}-- SSH
    {2}-- FTP
    {3}-- WordPress
    {4}-- G-Mail
    {5}-- Facebook
    {6}-- Zip File
    {7}-- Instagram
    {8}-- Twitter
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))

    if choice == 1:
        print('Not Ready For The Moment')
    elif choice == 99:
        menu()

def Osint():
    logo = colors.RANDOM + '''
     ___      _       _
    / _ \ ___(_)_ __ | |_
   | | | / __| | '_ \| __|
   | |_| \__ \ | | | | |_
    \___/|___/_|_| |_|\__|
    '''
    print(logo)
    tools = colors.RED + '''
    {1}-- Instagram Info
    {2}-- Twitter Info
    {3}-- Username LookUp
    {4}-- IP LookUp
    {5}-- Employee Search
    {6}-- Phone LookUp
    {7}-- Traceroute
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))

    if choice == 1:
        searchInstagram()
    elif choice == 2:
        searchTwitter()
    elif choice == 3:
        searchUserName()
    elif choice == 4:
        ipFinder()
    elif choice == 5:
        employee_lookup()
    elif choice == 6:
        phoneLookup()
    elif choice == 7:
        traceroute()
    elif choice == 99:
        menu()

def WirelessAttack():
    logo = colors.RANDOM + '''
    __        ___          _                    _   _   _             _
    \ \      / (_)_ __ ___| | ___  ___ ___     / \ | |_| |_ __ _  ___| | _____
     \ \ /\ / /| | '__/ _ \ |/ _ \/ __/ __|   / _ \| __| __/ _` |/ __| |/ / __|
      \ V  V / | | | |  __/ |  __/\__ \__ \  / ___ \ |_| || (_| | (__|   <\__ \\
       \_/\_/  |_|_|  \___|_|\___||___/___/ /_/   \_\__|\__\__,_|\___|_|\_\___/

    '''
    print(logo)
    tools = colors.RED + '''
    {1}-- Wireless Hijacking
    {2}-- DoS Attacks
    {3}-- Monitoring
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))

    if choice == 1:
        print('Not Ready For The Moment')
    elif choice == 99:
        menu()

def Anonymize():
    logo = colors.RANDOM + '''
        _                                      _
       / \   _ __   ___  _ __  _   _ _ __ ___ (_)_______
      / _ \ | '_ \ / _ \| '_ \| | | | '_ ` _ \| |_  / _ \\
     / ___ \| | | | (_) | | | | |_| | | | | | | |/ /  __/
    /_/   \_\_| |_|\___/|_| |_|\__, |_| |_| |_|_/___\___|
                               |___/
    '''
    print(logo)
    tools = colors.RED + '''
    {1}-- Set HTTP Proxy
    {2}-- Set HTTPS Proxy
    {3}-- Change MAC Adress
    {4}-- Enable Firewall
    {99}-- Exit
    '''
    print(tools)
    choice = int(input(prompt))
    if choice == 1:
        httpProxy()
    if choice == 2:
        httpsProxy()
    if choice == 3:
        macAdress()
    if choice == 4:
        os.system('ufw enable')
    if choice == 99:
        menu()

def Donation():
    donation()    

menu()
