from selenium import webdriver
import time
import os

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')
#Update the above line with the firefox installed path in your laptop
driver.get('https://www.linkedin.com/')
driver.maximize_window()
signin=driver.find_element_by_xpath('//a[@class="cta-modal__primary-btn"]')
time.sleep(1)
signin.click()
driver.find_element_by_id("username").send_keys(os.environ.get('LinkedIn_USER'))
#LinkedIn_USER is the environment variable to be used for username
time.sleep(1)
driver.find_element_by_id("password").send_keys(os.environ.get('LinkedIn_Pass'))
#LinkedIn_Pass is the environment variable to be used for password
time.sleep(1)
driver.find_element_by_css_selector('div.login__form_action_container').click()