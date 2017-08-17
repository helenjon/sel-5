from selenium import webdriver
from six_module.create_account_page import CreateAccount
from six_module import emailaddress
#import six_module.create_account_page
from six_module.accout_page import AccountPage
from six_module.litecart_main_page import MainPage 
from six_module.product_page import ProductPage
import time
from six_module.checkout import CheckoutPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class TestCreateAccount():
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8081/litecart/en/")
        self.driver.implicitly_wait(5)
        self.account = CreateAccount(self.driver)
        self.accountpage=AccountPage(self.driver)
        self.mainpage=MainPage(self.driver)
        self.checkoutpage=CheckoutPage(self.driver)
        self.emailaddress=emailaddress()
        self.productpage=ProductPage(self.driver)
        self.postcode=self.account.postcodes

    #def teardown_method(self):
    #    self.driver.quit()
    
  
    def testCreateAccount(self):
        self.mainpage.creatnewcustomer().click()
        self.account.TaxId().send_keys('test')
        self.account.FirstName().send_keys('test')
        self.account.LastName().send_keys('test')
        self.account.Company().send_keys('test')
        self.account.Address1().send_keys('test')
        if self.account.Country() != 'Andora':
            self.account.PostCode().send_keys('22022')
        else: self.account.PostCode().send_keys('21021')
        self.account.City().send_keys('Boston')
        self.account.Email().send_keys(self.emailaddress)
        self.account.Phone().send_keys('123456789')
        self.account.DesiredPassword().send_keys('welcome1')
        self.account.ConfirmPassword().send_keys('welcome1')
        self.account.Submit().click()
        self.accountpage.logout().click()
        self.driver.implicitly_wait(3)
        self.mainpage.emailaddress().send_keys(self.emailaddress)
        self.mainpage.password().send_keys('welcome1')
        self.mainpage.login().click()
        self.accountpage.logout().click()
        

    def testCreateAccountUS(self):
        self.mainpage.creatnewcustomer().click()   
        self.account.TaxId().send_keys('test')
        self.account.FirstName().send_keys('test')
        self.account.LastName().send_keys('test')
        self.account.Company().send_keys('test')
        self.account.Address1().send_keys('test')
        country=self.account.CountryUS()
        if country == 'United States':
            ZoneStatereturn=self.account.ZoneState()
            self.account.PostCode().send_keys(self.postcode[ZoneStatereturn])
        else: 
            self.account.Country()
            self.account.PostCode().send_keys('22022')
        self.account.City().send_keys('Boston')
        self.account.Email().send_keys(self.emailaddress)
        self.account.Phone().send_keys('123456789')
        self.account.DesiredPassword().send_keys('welcome1')
        self.account.ConfirmPassword().send_keys('welcome1')
        self.account.Submit().click()
        self.accountpage.logout().click()
        self.driver.implicitly_wait(3)
        self.mainpage.emailaddress().send_keys(self.emailaddress)
        self.mainpage.password().send_keys('welcome1')
        self.mainpage.login().click()
        self.accountpage.logout().click() 

    def testScenarioAddToBasket(self):
        self.driver.get('http://localhost:8081/litecart/en/')
        self.litecartmain=self.mainpage
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
                wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(quantityplass)))
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
        while quantity1>0:
            if len(self.driver.find_elements_by_xpath(".//a[@href='#']"))>0:
                self.driver.find_elements_by_xpath(".//a[@href='#']")[0].click()
            if len(str(self.checkoutpage.removebutton()))>0:
                self.checkoutpage.removebutton().click()
                time.sleep(5)
            else:
                self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Back').click()
            quantity1-=1
        #self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Back').click()
        time.sleep(20)
        
   
        

        

