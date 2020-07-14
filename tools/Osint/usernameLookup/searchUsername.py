import requests
from tools.Osint.usernameLookup.searchGoogle import searchGoogle
from colorama import init, Fore, Back, Style

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def searchUsername():
    username = input("Username: ")
    print("\n" + wait + " We Are Searching About The Username You Provided")

    url = "https://www.google.com/search?num=100&q=\\%s\\"
    url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
    requete = requests.get(url % (username))
    requete2 = requests.get(url2 % (username))
    searchGoogle(requete=requete, requete2=requete2)
    print("\n" + found + " The Result For The Username Search Are Stocked In: /home/yukio/Bureau/Umbradge/database/PossibleConnection.txt")
