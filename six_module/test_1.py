
#import random
#from django.template.defaultfilters import title
#from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time, requests, json
import pytest
from six_module.product_page import ProductPage
from six_module.litecart_main_page import MainPage
from six_module.checkout import CheckoutPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os
from PIL import Image
from six_module import data
import six_module





class Test():
        #return self.quantity_in_cart , self.value_in_cart
        
    def qtest3(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8081/litecart/en/')
        self.productpage=ProductPage(self.driver)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//div[@class='content']/ul[@class='listing-wrapper products']/li[1]/a[1]").click()
        quantity=self.driver.find_element_by_class_name('quantity')
        print quantity.get_attribute('textContent')
        self.driver.find_element_by_name("add_cart_product").click()
        time.sleep(10)
        quantity=self.driver.find_element_by_class_name('quantity')
        print quantity.get_attribute('textContent')
        #cart_value_added=cartcheck()[0]
        self.driver.find_element_by_xpath("//div[@class='content']/ul[@class='listing-wrapper products']/li[1]/a[1]").click()
    

    def qtest4(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8081/litecart/en/')
        self.productpage=ProductPage(self.driver)
        self.litecartmain=MainPage(self.driver)
        self.checkoutpage=CheckoutPage(self.driver)
        quantity=self.driver.find_element_by_class_name('quantity').get_property('textContent')
        wait = WebDriverWait(self.driver, 10)
        while int(quantity)<3:
            self.driver.find_element_by_xpath("//div[@class='content']/ul[@class='listing-wrapper products']/li[1]/a[1]").click()
            try:
                self.driver.find_element_by_xpath(".//*[@class='options']/strong") 
                select = Select(self.driver.find_element_by_name("options[Size]"))
                select.select_by_value('Small')
                self.productpage.addtocart().click()
                quantityplass=int(quantity)+1
                element = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(quantityplass)))
                quantity=self.driver.find_element_by_class_name('quantity').get_property('textContent')
            except:
                self.productpage.addtocart().click()
                quantityplass=int(quantity)+1
                element = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(quantityplass)))
                #print element 
                quantity=self.driver.find_element_by_class_name('quantity').get_property('textContent')
            self.productpage.linkhome().click()
        self.litecartmain.checkout().click()
        quantity1=int(quantity)
        print quantity1 
        while quantity1>0:
            if len(self.driver.find_elements_by_xpath(".//a[@href='#']"))>0:
                self.driver.find_elements_by_xpath(".//a[@href='#']")[0].click()
            print 'remove', str(self.checkoutpage.removebutton())    
            if len(str(self.checkoutpage.removebutton()))>0:
                self.checkoutpage.removebutton().click()
                time.sleep(5)
            else:
                self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Back').click()
            quantity1-=1
        time.sleep(20)
                
     
    def test5(self):
        list_of_titles=[
        "ISO 3166-1 alpha-2 - Wikipedia",    
        "ISO 3166-1 alpha-3 - Wikipedia",
        "Regular expression - Wikipedia",
        "International Proper Mailing Address Format | Informatica US",
        "Regular expression - Wikipedia",
        "List of countries and capitals with currency and language - Wikipedia",
        "List of country calling codes - Wikipedia"]
        driver = webdriver.Chrome()
        driver.get ('http://localhost:8081/litecart/admin/login.php')
        login=driver.find_element(By.NAME, 'username')
        login.send_keys('admin')
        password=driver.find_element(By.NAME, 'password')
        password.send_keys('admin')
        driver.find_element(By.NAME, 'login').click()
        driver.find_element_by_link_text('Countries').click()
        driver.find_element_by_link_text('Add New Country').click()
        time.sleep(5)
        links_from_page=driver.find_elements_by_xpath('//a[@target="_blank"]/i')
        links_from_page_for_test=links_from_page[3:]
        i=0
        j=1
        for all in links_from_page_for_test:
            all.click()
            driver.switch_to_window(driver.window_handles[-1])
            print str(driver.title), 'test',str(list_of_titles[i])
            assert str(driver.title) ==str(list_of_titles[i])
            i=i+1 
            driver.switch_to_window(driver.window_handles[0])
            time.sleep(10)
            
            
    def qtest6(self):       
        driver = webdriver.Chrome()
        driver.get("http://localhost:8081/litecart/en/")
        driver.save_screenshot("screenshot.png")
        #screen_name=str(driver.title)+'.png'
        #print 'screen_name', screen_name 
        #driver.save_screenshot('D:\\GitHub\\sel-5\\six_module\\%s' %screen_name )
        #links_test=driver.find_elements_by_xpath(".//a[@class='link' and @title]")
        
            
        
        
        
    def qtest7(self):    
        driver = webdriver.Chrome()
        driver.get("http://localhost:8081/litecart/en/")
        actions = ActionChains(driver)
        curWindowHndl = driver.current_window_handle
        about = driver.find_elements_by_xpath(".//*[@id='box-most-popular']/div/ul/li/a[1]")
        print about
        
        for all in range(len(about)):
            actions.key_down(Keys.CONTROL).click(about[all]).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
            print driver.title
            assert str(driver.title) == str(driver.title)
            driver.close()
            driver.switch_to.window(driver.window_handles[0]) #closes new tab
            #driver.switch_to_window(curWindowHndl)
            print driver.title 
        #    about = driver.find_elements_by_xpath(".//*[@id='box-most-popular']/div/ul/li/a[1]")
            time.sleep(10)
            
            
    def test8(self):
        driver = webdriver.Chrome()
        driver.get("https://workbench.dnb.com/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, ".//*[@id='mainContent']/div/div[2]/div[1]/a")))
        try :
            w=driver.find_element(By.XPATH, ".//*[@id='mainContent']/div/div[2]/div[1]/ul/li[3]")
            print w.get_attribute('textContent')
            print driver.title
            screen_name=str(driver.title)+'.png'
            print 'screen_name', screen_name 
            driver.save_screenshot('D:\\GitHub\\sel-5\\six_module\\%s' %screen_name )
            driver.find_element(By.XPATH, ".//a[@class='btn btn-3d-large modal-trigger btn-blue']").click()
        except NoSuchElementException:
            print 'test'
        driver.close()
        
        
    def test9(self):
        driver = webdriver.Firefox()
        driver.get('http://www.python.org/')
        driver.save_screenshot('python_org.png')
        driver.quit()
          
    
    
        
class TestAdmin():
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        
    
    def test(self):
        url = "http://www.python.org/"
        self.driver.get(url)
        Test().fullpage_screenshot(self.driver, "test.png")
        
        
           

def test77():
 



        
    
        