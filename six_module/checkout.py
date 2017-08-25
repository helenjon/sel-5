from selenium.webdriver.common.by import By

class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        
    
    def removebutton(self):
        return self.driver.find_element(By.NAME, 'remove_cart_item')
    