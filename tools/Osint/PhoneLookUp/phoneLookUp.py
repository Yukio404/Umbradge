import requests
import os
import sys
import urllib
import json

def phoneLookup():
    k = '\033[93m'
    u = '\033[95m'
    n  = '\033[94m'
    m = '\033[91m'
    h = '\033[92m'
    p = '\033[00m'

    number = input(m+"["+k+"#"+m+"]"  +h+"Phone Number: ")
    countryCode = input(m + "[" + k + "#" + m + "]" + h + "Country Code (2 Letters, EX: GB): ")
    print("\n")
    #data
    key = "9810ba5ae4fe74c2930842025d11bc58"
    url = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + number + "&country_code=" + countryCode + "&format=1"
    output = requests.get(url)
    result = output.text
    js = json.loads(result)

    country_code = js['country_code']
    country_name = js['country_name']
    location = js['location']
    carrier = js['carrier']
    line_type = js['line_type']

    print(m+"["+k+"#"+m+"]"  +h+"phonenumber information gathering"  +m+"["+k+"#"+m+"]")
    print("\n")
    print (k+"["+m+"+"+k+"]"  +h+" Information Output")
    print(k+"--------------------------------------")
    print(k+" ~" +h+" Phone number: " +str(number))
    print(k+" ~" +h+" Country: " +str(country_code))
    print(k+" ~" +h+" Country Name: " +str(country_name))
    print(k+" ~" +h+" Location: " +str(location))
    print(k+" ~" +h+" Carrier: " +str(carrier))
    print(k+" ~" +h+" Device: " +str(line_type))
