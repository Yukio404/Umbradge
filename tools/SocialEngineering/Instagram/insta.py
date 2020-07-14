from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By
from tools.SocialEngineering.Instagram import config as account
from selenium.webdriver.chrome.options import Options

def createAccount():
    password = input('Enter Your Password: ')

    print("We Are Generating Your Account...")


    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    browser= webdriver.Chrome("chromedriver", chrome_options = chrome_options)
    browser.get("http://localhost:3001/")
    time.sleep(2) #time.sleep count can be changed depending on the Internet speed.
    name = account.username()

    #Fill the email value
    email_field = browser.find_element_by_name('emailOrPhone')
    email_field.send_keys(account.generatingEmail())
    print(account.generatingEmail())

    #Fill the fullname value
    fullname_field = browser.find_element_by_name('fullName')
    fullname_field.send_keys(account.generatingName())
    print(account.generatingName())
    #Fill username value
    username_field = browser.find_element_by_name('username')
    username_field.send_keys(name)
    print(name)
    #Fill password value
    password_field  = browser.find_element_by_name('password')
    password_field.send_keys(password) #You can determine another password here.
    print(password)

    submit = browser.find_element(By.CSS_SELECTOR, "form button")
    submit.click()
    time.sleep(8)

    print('Registering....')
