from selenium import webdriver
import time
import sys

PATH = "_____"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(PATH, chrome_options=options)

# driver = webdriver.Chrome(PATH)
driver.get("https://cyberoam.daiict.ac.in:8090/httpclient.html")

input_username = driver.find_element_by_id('username')
input_password = driver.find_element_by_id('password')
login_btn = driver.find_element_by_id('loginbutton')


input_username.send_keys('_____')
input_password.send_keys('_____')
login_btn.click()

sys.exit(0)