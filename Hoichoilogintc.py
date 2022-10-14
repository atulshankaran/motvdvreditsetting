from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

# it is a url of web which is going to open in selenium
WEBSITE_URL = "https://hoichoi.tv" 

EMAIL_TO_LOGIN = "mrinal@viewlift.com"
EMAIL_TO_LOGIN_PASS = "123456"
# ALWAYS USE VARIABLE, DO NOT HARDCODE VALUES
driver.get(WEBSITE_URL)

driver.implicitly_wait(20)

LOGIN_BUTTON = driver.find_element(by=By.CSS_SELECTOR, value="#root > div > div.header-container > div > div > div.header-secondary-menu > ul > li:nth-child(2) > span")

LOGIN_BUTTON.click()

driver.implicitly_wait(20)


EMAIL_LOGIN_BUTTON = driver.find_element(By.CSS_SELECTOR, "#root > div > div.header-container > div > div.otp-login-container.show > div > div.otp-login-parent > div > div.otp-login-social-login-container > div.otp-login-social-login-options > div:nth-child(4)")

EMAIL_LOGIN_BUTTON.click()



EMAIL_INPUT = driver.find_element(By.CSS_SELECTOR, "#email-login-mob-email")

EMAIL_INPUT.send_keys(EMAIL_TO_LOGIN)

PASSWORD_INPUT = driver.find_element(By.CSS_SELECTOR, "#email-login-password")

PASSWORD_INPUT.send_keys(EMAIL_TO_LOGIN_PASS)

SUBMIT_BTN = driver.find_element(By.CSS_SELECTOR, "#root > div > div.header-container > div > div.otp-login-container.show > div > div.otp-login-parent > div > div.email-login-container > div > div > div > div > div:nth-child(3) > button")

SUBMIT_BTN.click()

sleep(10)

