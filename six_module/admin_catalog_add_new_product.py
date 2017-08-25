from selenium import webdriver
from selenium.webdriver.common.by import By
from six_module.admin_main import LiteCartMain


class AddNewProduct():
    
    def __init__(self, driver):
        self.driver=driver

    def StatusEnable(self):
        return self.driver.find_element_by_xpath(".//*[@name='status' and @value='1']")
    
    def StatusDisabled(self):
        return self.driver.find_element_by_xpath(".//*[@name='status' and @value='0']")
    
    def Categories(self):
        return self.driver.find_element_by_xpath(".//*[@name='categories[]' and @value='3']")
     
        
    def Name(self):
        return self.driver.find_element_by_name("name[en]")
    
    def Code(self):
        return self.driver.find_element_by_name('code')
    
    def ProductGroups(self):
        return self.driver.find_element_by_xpath('.//*[@name="product_groups[]" and @value="1-2"]')
    
    
    def Quantity(self):
        return self.driver.find_element_by_name('quantity')
    
    def DateValidFrom(self):
        return self.driver.find_element_by_name('date_valid_from')
        
    def DateValidTo(self):
        return self.driver.find_element_by_name('date_valid_to')
    
    
    def Save(self):
        return self.driver.find_element_by_name('save')
        
    def Cancel(self):
        return self.driver.find_element_by_name('cancel')
    
    def Delete(self):
        return self.driver.find_element_by_name('delete')