import email
from time import sleep, time
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
"""from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

WEBSITE_URL = "https://www.hoichoi.tv/" 



#driver.get(WEBSITE_URL)

#driver.implicitly_wait(5)"""

#opening jsson file

f = open('data.json')

#return json file as dictionary

data = json.load(f)

#iterating json data in python program

for mails in data['email']:
    print(mails)

for password in data['pass']:
    print(password)
    



