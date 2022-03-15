from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# Enter the path to your selenium webdrive (Chromedriver here)
# Although this method is being depricated and it is recommended to use Service, we will learn this for now since this is simple.
driver = webdriver.Chrome("path")
driver.get("https://forms.gle/whiPHrhC5XAb96QQ7")

# Fill email-id
email_field = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

email_field.click()
email_field.send_keys("test@gmail.com")

# Fill name
name_field = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))

name_field.click()
name_field.send_keys("John Doe")

# Fill favourite Color
textbox = driver.find_element(By.ID, "i13").click()

# select favourite language from dropdown
driver.find_element(By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]').click()

drop_select = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]')))

drop_select.click()

time.sleep(2)

# Click on submit button
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))

submit_button.click()
