from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support.wait import WebDriverWait


def exception(driver):
    try:
        driver.find_element(By.TAG_NAME, 'h1')
        print 'pass'
    except NoSuchElementException:
        print 'No such thing'
        
driver=webdriver.Chrome()
driver.implicitly_wait(10)
admin_url ='http://localhost:8081/litecart/admin/login.php' 

driver.get(admin_url)
login=driver.find_element(By.NAME, 'username')
password=driver.find_element(By.NAME, 'password')
login.send_keys("admin")
password.send_keys('admin')
loginbutton=driver.find_element(By.NAME, 'login')
loginbutton.click()

links=driver.find_elements(By.XPATH, '//*[@id="app-"]/a')
for i in range(16):
    links[i].click()
    podcatalog=driver.find_elements(By.XPATH,".//ul[@class='docs']/li/a/span")
    driver.implicitly_wait(10)
    j=0 
    if len(podcatalog)>0:
        for j in range(len(podcatalog)):
            podcatalog[j].click()
            podcatalog=driver.find_elements(By.XPATH,".//ul[@class='docs']/li/a/span")
            exception(driver)
            
    exception(driver)
    main_link=driver.find_element(By.CLASS_NAME, 'logotype')
    main_link.click()  
    links=driver.find_elements(By.XPATH, '//*[@id="app-"]/a')
driver.close()
    
    
    

    

     

    
    
               
               




