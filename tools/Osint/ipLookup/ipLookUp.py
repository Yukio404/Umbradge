import ipinfo
from colorama import init, Fore, Back, Style

def ipLookup():
    access_token = 'aba7981627ae8a'
    handler = ipinfo.getHandler(access_token)
    ip_address = input("IP Adress: ")

    details = handler.getDetails(ip_address)
    city = details.city
    loc = details.loc
    country = details.country_name
    longitude = details.longitude
    latitude = details.latitude

    warning = "["+Fore.RED+"!"+Fore.RESET+"]"
    question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
    found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
    wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

    print("\n" + found + "City: " + city)
    print("\n" + found + "Location" + loc)
    print("\n" + found + "Country: " + country)
    print("\n" + found + "Lognitude: " + longitude)
    print("\n" + found + "Latitude: " + latitude)
