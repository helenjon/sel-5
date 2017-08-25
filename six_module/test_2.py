from PIL import Image
from selenium import webdriver 
import os, time
    




class TestAdmin():
    
    def setup_method(self):
        self.driver = webdriver.Firefox()
        
    def test1(self):
        url = "http://www.python.org/"
        self.driver.get(url)
        self.fullpage_screenshot(self.driver, "test.png")
   
    
        
        
        
