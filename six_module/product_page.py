from selenium.webdriver.common.by import By

class ProductPage():
    def __init__(self, driver):
        self.driver = driver
        
    
    def linkhome(self):
        return self.driver.find_element(By.LINK_TEXT, 'Home')
    
    def addtocart(self):    
        return self.driver.find_element(By.NAME, 'add_cart_product')