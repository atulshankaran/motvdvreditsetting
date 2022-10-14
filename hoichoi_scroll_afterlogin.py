from time import sleep, time
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# it is a url of web which is going to open in selenium
WEBSITE_URL = "https://www.hoichoi.tv/" 

EMAIL_TO_LOGIN = "mrinal@viewlift.com"
EMAIL_TO_LOGIN_PASS = "123456"

# ALWAYS USE VARIABLE, DO NOT HARDCODE VALUES

driver.get(WEBSITE_URL)

driver.implicitly_wait(5)


sleep(3)

driver.execute_script("window.scrollTo(0,1000)")

sleep(5)

driver.execute_script("window.scrollTo(1000,2000)")

sleep(5)
driver.execute_script("window.scrollTo(2000,3000)")

sleep(5)

driver.execute_script("window.scrollTo(3000,4000)")

sleep(5)
driver.execute_script("window.scrollTo(4000,5000)")

sleep(5)
driver.execute_script("window.scrollTo(5000,6000)")

sleep(5)

driver.execute_script("window.scrollTo(6000,7000)")

sleep(5)

driver.execute_script("window.scrollTo(7000,8000)")

sleep(5)

driver.execute_script("window.scrollTo(8000,9000)")

sleep(5)


LOGIN_BUTTON = driver.find_element(by=By.CSS_SELECTOR, value="#root > div > div > div.modules.undefined > div:nth-child(2) > nav > div > header > div.controls > button")

LOGIN_BUTTON.click()

driver.implicitly_wait(3)


EMAIL_LOGIN_BUTTON = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.popup-view.type-login > div:nth-child(1) > div.auth-view02.centered02 > div.social-logins > div > button.phoneButton.button.fat")

EMAIL_LOGIN_BUTTON.click()

EMAIL_INPUT = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.popup-view.type-login > div:nth-child(1) > div.auth-view02.centered02 > form > div:nth-child(2) > input[type=email]")

EMAIL_INPUT.send_keys(EMAIL_TO_LOGIN)

PASSWORD_INPUT = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.popup-view.type-login > div:nth-child(1) > div.auth-view02.centered02 > form > div:nth-child(3) > input[type=password]")

PASSWORD_INPUT.send_keys(EMAIL_TO_LOGIN_PASS)

SUBMIT_BTN = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.popup-view.type-login > div:nth-child(1) > div.auth-view02.centered02 > form > div:nth-child(5) > input")

SUBMIT_BTN.click()

sleep(3)

driver.execute_script("window.scrollTo(0,1000)")

sleep(6)

driver.execute_script("window.scrollTo(1000,2000)")

sleep(6)
driver.execute_script("window.scrollTo(2000,3000)")

sleep(6)

driver.execute_script("window.scrollTo(3000,4000)")

sleep(6)
driver.execute_script("window.scrollTo(4000,5000)")

sleep(6)
driver.execute_script("window.scrollTo(5000,6000)")

sleep(6)

driver.execute_script("window.scrollTo(6000,7000)")

sleep(6)

driver.execute_script("window.scrollTo(7000,8000)")

sleep(6)

driver.execute_script("window.scrollTo(8000,9000)")

sleep(6)

driver.execute_script("window.scrollTo(9000,10000)")

sleep(6)

driver.execute_script("window.scrollTo(10000,0)")

sleep(6)

Later_button = driver.find_element(By.CSS_SELECTOR, "#wzrk-cancel")

Later_button.click()

sleep(6)

upcoming_btn = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.modules.undefined > div:nth-child(2) > nav > div > header > div.large-version.left > nav > div:nth-child(4) > span > a > span")

upcoming_btn.click()

sleep(5)

driver.execute_script("window.scrollTo(0,1000)")

sleep(3)

driver.execute_script("window.scrollTo(1000,2000)")

sleep(3)
driver.execute_script("window.scrollTo(2000,3000)")

sleep(3)

driver.execute_script("window.scrollTo(3000,4000)")

sleep(3)
driver.execute_script("window.scrollTo(4000,0)")

sleep(3)

gift_btn = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.modules.undefined > div:nth-child(2) > nav > div > header > div.large-version.left > nav > div:nth-child(5) > span > a > span") 

gift_btn.click()

driver.execute_script("window.scrollTo(0,1000)")

sleep(3)

driver.execute_script("window.scrollTo(1000,2000)")

sleep(3)

hoichoitech_btn = driver.find_element(By.CSS_SELECTOR, "#root > footer > div > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-4 > div > a > img")

hoichoitech_btn.click()

sleep(5)

back_to_hoichoi = driver.find_element(By.CSS_SELECTOR, "#navbarSupportedContent > div > a")

back_to_hoichoi.click()

sleep(60)