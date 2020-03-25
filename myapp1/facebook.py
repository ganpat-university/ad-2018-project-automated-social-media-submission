import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\\Chromedriver.exe")
driver.get('https://www.facebook.com/')
mail_element = driver.find_element(By.XPATH, './/*[@id="email"]')
mail_element.send_keys('08320113199')
pass_element = driver.find_element(By.XPATH, './/*[@id="pass"]')
pass_element.send_keys('Kush1212')

elem = driver.find_element(By.XPATH, './/*[@id="loginbutton"]')
elem.click()

statuselement = driver.find_element(By.XPATH, "//*[@name='xhpc_message']")
time.sleep(5)

statuselement.send_keys("Helloo...")
time.sleep(5)
buttons = driver.find_elements_by_tag_name('button')
time.sleep(5)

for button in buttons:
    if button.text == 'Post':
        button.click()
