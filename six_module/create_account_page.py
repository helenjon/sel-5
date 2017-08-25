from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import Select
from six_module import configparserr




class CreateAccount():
    
    def __init__(self, driver):
        self.driver = driver
        self.usstate=['AL','AK','AS','AZ','AR','AF','AA','AC','AE','AM','AP','CA','CO','CT','DE','DC','FM','FL','GA','GU','HI','ID','IL','IN','IA','KS','KY','LA','ME','MH','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','MP','OH','OK','OR','PW','PA','PR','RI','SC','SD','TN','TX','UT','VT','VI','VA','WA','WV','WI','WY']
        self.postcodes={'AL':10001,'AK':10002,'AS':10065,'AZ':10003,'AR':10004,'AF':10005,'AA':10006,'AC':10007,'AE':10008,'AM':10009,'AP':10010,'CA':10011,'CO':10012,'CT':10013,'DE':10014,'DC':10015,'FM':10016,'FL':10017,'GA':10018,'GU':10019,'HI':10020,'ID':10021,'IL':10022,'IN':10023,'IA':10024,'KS':10025,'KY':10026,'LA':10027,'ME':10028,'MH':10029,'MD':10030,'MA':10031,'MI':10032,'MN':10033,'MS':10034,'MO':10035,'MT':10036,'NE':10037,'NV':10038,'NH':10039,'NJ':10040,'NM':10041,'NY':10042,'NC':10043,'ND':10044,'MP':10045,'OH':10046,'OK':10047,'OR':10048,'PW':10049,'PA':10050,'PR':10051,'RI':10052,'SC':10053,'SD':10054,'TN':10055,'TX':10056,'UT':10057,'VT':10058,'VI':10059,'VA':10060,'WA':10061,'WV':10062,'WI':10063,'WY':10064}

    def TaxId (self):
        return self.driver.find_element(By.NAME, 'tax_id')
            
    def Company(self):
        return self.driver.find_element(By.NAME, 'company')
    
    def FirstName(self):
        return self.driver.find_element(By.NAME, 'firstname')
    
    def LastName(self):
        return self.driver.find_element(By.NAME, 'lastname')
    
    def Address1(self):
        return self.driver.find_element(By.NAME, 'address1')
    
    def Address2(self):
        return self.driver.find_element(By.NAME, 'address2')
    
    def PostCode(self):
        return self.driver.find_element(By.NAME, 'postcode')
    
    def City(self):
        return self.driver.find_element(By.NAME, 'city')
    
    def Email(self):
        return self.driver.find_element(By.NAME, 'email')
    
    def Phone(self):
        return self.driver.find_element(By.NAME, 'phone')
    
    def DesiredPassword(self):
        return self.driver.find_element(By.NAME, 'password')
    
    def ConfirmPassword(self):
        return self.driver.find_element(By.NAME, 'confirmed_password')
    
    
    def Submit(self):
        return self.driver.find_element(By.NAME, 'create_account')
    
    def Newsletter(self):
        return self.driver.find_element(By.NAME, 'newsletter')
    
    def Country(self):
        self.driver.find_element(By.XPATH, ".//*[@id='create-account']/div/form/table/tbody/tr[5]/td[1]/span[2]/span[1]/span/span[2]").click()
        ww=self.driver.find_elements(By.CLASS_NAME, 'select2-results__option')
        ww[random.randrange(1, len(ww))].click()
        self.driver.implicitly_wait(5)
        return self.driver.find_element(By.XPATH, ".//*[@class='select2-selection__rendered']").get_attribute('title')
        #return self.ww[random.randrange(1, len(ww))]

    def CountryUS(self): 
        self.driver.find_element(By.XPATH, ".//*[@id='create-account']/div/form/table/tbody/tr[5]/td[1]/span[2]/span[1]/span/span[2]").click()
        ww =self.driver.find_elements(By.CLASS_NAME, 'select2-results__option')
        ww[224].click()
        return self.driver.find_element(By.XPATH, ".//*[@class='select2-selection__rendered']").get_attribute('title')
            
    def ZoneState(self):
        #self.driver.find_element(By.XPATH, ".//*[@id='create-account']/div/form/table/tbody/tr[5]/td[2]/select").click()
        #ww=self.driver.find_elements(By.NAME, 'zone_code')
        usstateval_add=self.usstate[random.randrange(1, len(self.usstate))]
        Select(self.driver.find_element_by_xpath("//select[@name='zone_code']")).select_by_value(usstateval_add)
        return usstateval_add
        
    

       
    
    
    
    
    
    
    
    
    
    