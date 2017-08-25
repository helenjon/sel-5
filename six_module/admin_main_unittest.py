from selenium import webdriver
from selenium.webdriver.common.by import By
import logging, time
from six_module.admin_litecart_catalog_page import LiteCartCatalogPage
from six_module.admin_main import LiteCartMain 
from six_module.admin_catalog_add_new_product import  AddNewProduct
from parse_conf import ParseConfig
from six_module import randomValueProductQuantity, data



class TestAdmin():
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        #admin_url ='http://localhost:8081/litecart/admin/login.php'
        logging.basicConfig(level=logging.DEBUG)
        #self.log = logging.getLogger('test9') 
        self.driver.implicitly_wait(5)
        self.driver.get ("http://"+ParseConfig().admin_url)
        #self.driver.get ('http://localhost:8081/litecart/admin/login.php')
        login=self.driver.find_element(By.NAME, 'username')
        login.send_keys(ParseConfig().admin_login)
        password=self.driver.find_element(By.NAME, 'password')
        #login.send_keys('admin')
        password.send_keys(ParseConfig().admin_password)
        #password.send_keys('admin')
        loginbutton=self.driver.find_element(By.NAME, 'login')
        loginbutton.click()
        self.litecartmain=LiteCartMain(self.driver)
        self.litecartcatalog=LiteCartCatalogPage(self.driver)
        self.addnewproduct=AddNewProduct(self.driver)
     
    def wtestAddNewProduct(self):
        self.litecartmain.mainmenulinks()[1].click()
        self.litecartcatalog.addnewproduct().click()
        self.addnewproduct.StatusEnable().click()
        self.addnewproduct.Name().send_keys('test_'+ParseConfig().count_product)
        self.addnewproduct.Code().send_keys(ParseConfig().count_product)
        self.addnewproduct.Categories().click()
        self.addnewproduct.Quantity().clear()
        self.addnewproduct.Quantity().send_keys(str(randomValueProductQuantity()))
        self.driver.implicitly_wait(300)
        self.addnewproduct.ProductGroups().click()
        self.addnewproduct.DateValidFrom().send_keys('05/10/2017')
        self.addnewproduct.DateValidTo().send_keys('05/10/2018')
        self.addnewproduct.Save().click()
        count_product= str(int(ParseConfig().count_product)+1)
        ParseConfig().parse_file_set(count_product)
    
    
    def testnamber14(self):
        self.driver.find_element_by_link_text('Countries').click()
        self.driver.find_element_by_link_text('Add New Country').click()
        time.sleep(5)
        links_from_page=self.driver.find_elements_by_xpath('//a[@target="_blank"]/i')
        links_from_page_for_test=links_from_page[3:]
        i=0
        j=1
        for all in links_from_page_for_test:
            all.click()
            self.driver.switch_to_window(self.driver.window_handles[-1])
            #print str(self.driver.title), 'test',str(ParseConfig().list_of_titles[i])
            assert str(self.driver.title) ==str(ParseConfig().list_of_titles[i])
            i=i+1 
            self.driver.switch_to_window(self.driver.window_handles[0])
            time.sleep(10)
        
        

    
    