from selenium import webdriver
from selenium.webdriver.common.by import By


admin_url ='http://localhost:8081/litecart/admin/login.php' 
driver=webdriver.Firefox()
driver.implicitly_wait(200)
driver.get(admin_url)
login=driver.find_element(By.NAME, 'username')
password=driver.find_element(By.NAME, 'password')
login.send_keys("admin")
password.send_keys('admin')


driver.close()