from selenium import webdriver
from selenium.webdriver.common.by import By


class LiteCartMain():
    
    def __init__(self, driver):
        self.driver=driver
        
        
    def mainmenulinks(self):
        return self.driver.find_elements(By.XPATH, '//*[@id="app-"]/a') 
    