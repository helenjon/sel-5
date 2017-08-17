from selenium import webdriver
from selenium.webdriver.common.by import By 

class AccountPage():
    
    def __init__(self, driver):
        self.driver = driver
        
        
    def customerService(self):
        pass
    
    
    def orderHistory(self):
        pass
    
    def editAccount(self):
        pass
    
    def logout(self):
        return self.driver.find_element(By.XPATH, ".//*[@id='box-account']/div/ul/li[4]/a")
        
    