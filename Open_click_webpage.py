from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')
driver.get('https://www.google.com/')
corona = driver.find_element_by_id('prm')
corona.click()