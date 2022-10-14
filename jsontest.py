from select import select
from time import sleep, time
from tkinter.tix import Select
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#using json for fetching data

import json

f = open('data.json')


#return json file as dictionary

data = json.load(f)

#iterating json data in python program

for mails in data['email']:
    print()

for password in data['pass']:
    print(password)


sleep(10)
