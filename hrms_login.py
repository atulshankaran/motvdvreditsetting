from time import sleep, time
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# it is a url of web which is going to open in selenium
WEBSITE_URL = "https://hrms.nexgsolution.com/admin/" 

EMAIL_TO_LOGIN = "atul@nexgsolution.com"
EMAIL_TO_LOGIN_PASS = "9625465694"

# ALWAYS USE VARIABLE, DO NOT HARDCODE VALUES

driver.get(WEBSITE_URL)

sleep(5)

LOGIN_BUTTON = driver.find_element(by=By.CSS_SELECTOR, value="#root > div > div > div.modules.undefined > div:nth-child(2) > nav > div > header > div.controls > button")

LOGIN_BUTTON.click()

sleep(2)


EMAIL_LOGIN_BUTTON = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.popup-view.type-login > div:nth-child(1) > div.auth-view02.centered02 > div.social-logins > div > button.phoneButton.button.fat > span")

EMAIL_LOGIN_BUTTON.click()

EMAIL_INPUT = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.popup-view.type-login > div:nth-child(1) > div.auth-view02.centered02 > form > div:nth-child(2) > input[type=email]")

EMAIL_INPUT.send_keys(EMAIL_TO_LOGIN)

PASSWORD_INPUT = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.popup-view.type-login > div:nth-child(1) > div.auth-view02.centered02 > form > div:nth-child(3) > input[type=password]")

PASSWORD_INPUT.send_keys(EMAIL_TO_LOGIN_PASS)

SUBMIT_BTN = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.popup-view.type-login > div:nth-child(1) > div.auth-view02.centered02 > form > div:nth-child(5) > input")

SUBMIT_BTN.click()
