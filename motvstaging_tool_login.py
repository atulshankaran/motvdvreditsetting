from select import select
from time import sleep, time
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# it is a url of web which is going to open in selenium
WEBSITE_URL = "https://staging-tools.viewlift.com/" 

EMAIL_TO_LOGIN = "atulshankaran+staging.motv@viewlift.com"
EMAIL_TO_LOGIN_PASS = "Shankaran@06"
# ALWAYS USE VARIABLE, DO NOT HARDCODE VALUES
driver.get(WEBSITE_URL)

driver.implicitly_wait(20)

#LOGIN_BUTTON = driver.find_element(by=By.CSS_SELECTOR, value="#root > div > div.header-container > div > div > div.header-secondary-menu > ul > li:nth-child(2) > span")

#LOGIN_BUTTON.click()

#driver.implicitly_wait(20)


#EMAIL_LOGIN_BUTTON = driver.find_element(By.CSS_SELECTOR, "#root > div > div.header-container > div > div.otp-login-container.show > div > div.otp-login-parent > div > div.otp-login-social-login-container > div.otp-login-social-login-options > div:nth-child(4)")

#EMAIL_LOGIN_BUTTON.click()



EMAIL_INPUT = driver.find_element(By.CSS_SELECTOR, "#username")

EMAIL_INPUT.send_keys(EMAIL_TO_LOGIN)

PASSWORD_INPUT = driver.find_element(By.CSS_SELECTOR, "#password")

PASSWORD_INPUT.send_keys(EMAIL_TO_LOGIN_PASS)

SUBMIT_BTN = driver.find_element(By.CSS_SELECTOR, "#loginsubmit")

SUBMIT_BTN.click()

x
#user will click on content

CONTENT_BUTTON = driver.find_element(By.CSS_SELECTOR, "#contenttab")

CONTENT_BUTTON.click()

sleep(5)

ADDNEW_BUTTON = driver.find_element(By.CSS_SELECTOR, "#drag-container > label > div.dropdown-video > div.dd-button")

ADDNEW_BUTTON.click()

sleep(5)

LIVE_BTN = driver.find_element(By.CSS_SELECTOR, value="#liveEventButton")

LIVE_BTN.click()

sleep(5)

CANC_BTN = driver.find_element(By.CSS_SELECTOR, "#liveSection-part-one > div > div.buttonsWrapper > div.firstButton")

CANC_BTN.click()

sleep(5)

ADDNEW_BUTTON = driver.find_element(By.CSS_SELECTOR, "#drag-container > label > div.dropdown-video > div.dd-button")

ADDNEW_BUTTON.click()

sleep(5)


LIVE_BTN = driver.find_element(By.CSS_SELECTOR, value="#liveEventButton")

LIVE_BTN.click()

sleep(5)

AWS_RGN = driver.find_element(By.CSS_SELECTOR, "#awsRegion")

AWS_RGN_select = Select(AWS_RGN)

AWS_RGN_select.select_by_index(1)


sleep(5)

SLCT_PRTCL = driver.find_element(By.CSS_SELECTOR, "#protocols")

PRTCL = Select(SLCT_PRTCL)

PRTCL.select_by_index(1)

sleep(5)

HLS_URL = driver.find_element(By.CSS_SELECTOR, "#liveSection-part-one > div > div.hls-url-wrapper > div:nth-child(1) > div:nth-child(2) > input")

#hls url which will used for dvr

URL_hls = "https://cph-p2p-msl.akamaized.net/hls/live/2000341/test/master.m3u8"



HLS_INPUT_URL = driver.find_element(By.CSS_SELECTOR, "#liveSection-part-one > div > div.hls-url-wrapper > div:nth-child(1) > div:nth-child(2) > input")

HLS_INPUT_URL.send_keys(URL_hls) 

sleep(5)

DVR_S = driver.find_element(By.CSS_SELECTOR, "#liveSection-part-one > div > div.output-wrapper > div.radioDvrSection")

DVR_S.click()

sleep(2)

DVR_YES = driver.find_element(By.CSS_SELECTOR, "#liveSection-part-one > div > div.output-wrapper > div.radioDvrSection > div.radio-buttons > input.firstInput")

DVR_YES.click()

sleep(2)

DVR_INPUT_BOX = driver.find_element(By.CSS_SELECTOR, "#liveSection-part-one > div > div.dvr-wrapper > div > input")

DVR_INPUT_BOX.click()

DVR_Time = 7200

DVR_INPUT_BOX.send_keys(DVR_Time)

CRT_BTN = driver.find_element(By.CSS_SELECTOR, "#createLiveEvent")

CRT_BTN.click()


sleep(100)
