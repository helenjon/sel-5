from selenium import webdriver

driver=webdriver.Firefox()
driver.implicitly_wait(200)
driver.get('http://software-testing.ru')
driver.close()


