class LiteCartCatalogPage():
    
    def __init__(self, driver):
        self.driver=driver
        
        
        
    def addnewcategory(self):
        return self.driver.find_element_by_link_text('Add New Category')
    
    def addnewproduct(self):
        return self.driver.find_element_by_link_text('Add New Product')
    #//a[contains(text(),'Add New Category')]
    
    def productcheckbocks(self):
        return self.driver.find_element_by_tag_name(".//input[@name='products[6]']")
        