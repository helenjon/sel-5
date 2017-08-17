from selenium.webdriver.common.by import By

class MainPage():
    def __init__(self, driver):
        self.driver = driver
        
    
    def emailaddress(self):
        return self.driver.find_element(By.NAME, 'email')
    
    
    def password(self):
        return self.driver.find_element(By.NAME, 'password')
    
    def login(self):
        return self.driver.find_element(By.NAME, 'login')
    
    
    def lostpassword(self):
        return self.driver.find_element(By.NAME, 'lost_password')
        
    def creatnewcustomer(self):
        return self.driver.find_element_by_partial_link_text('New customers click here')
    
    def mostpopular(self):
        return self.driver.find_elements() 
    
    def checkout(self):
        return self.driver.find_element_by_partial_link_text('Checkout')