from time import time
import random
from django.template.defaultfilters import title
from selenium.webdriver.support.ui import Select
from ConfigParser import ConfigParser
from parse_conf import ParseConfig
import json, requests



def data():
    usstate=['AL','AK','AS','AZ','AR','AF','AA','AC','AE','AM','AP','CA','CO','CT','DE','DC','FM','FL','GA','GU','HI','ID','IL','IN','IA','KS','KY','LA','ME','MH','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','MP','OH','OK','OR','PW','PA','PR','RI','SC','SD','TN','TX','UT','VT','VI','VA','WA','WV','WI','WY']
    admin='admin'   
    list_of_titles=[
        "ISO 3166-1 alpha-2 - Wikipedia",    
        "ISO 3166-1 alpha-3 - Wikipedia",
        "Regular expression - Wikipedia",
        "International Proper Mailing Address Format | Informatica US",
        "Regular expression - Wikipedia",
        "List of countries and capitals with currency and language - Wikipedia",
        "List of country calling codes - Wikipedia"]

def configparserr():
    config = ConfigParser()
    config.read('option.ini')
    usstate_val = config.get('section', 'usstate')
    postcodes_val= config.get('section', 'postcodes')
    #print str(random.sample(usstate_val.split(','), 1 ))
    usstateval_add=str(random.sample(usstate_val.split(','), 1 ))[2:4]
    json_acceptable_string = postcodes_val.replace("'", "\"")
    postcodes_val_dic = json.loads(json_acceptable_string)
    return usstateval_add, postcodes_val_dic
    #postcodes_val_dic[usstateval_add]
    #print postcodes_val_dic[usstateval_add]

def emailaddress():
    emailaddresss='test'+str(int(round(time())))+'@test.com'
    return emailaddresss

def randomValueProductQuantity():
    randomValueProductQuantity= random.randrange(1000)
    return randomValueProductQuantity
    
def cartcheck():
    cart_responce = requests.get('http://localhost:8081/litecart/en/ajax/cart.json')
    result = json.loads(cart_responce.text)  # result is now a dict
    quantity_in_cart = str(result['quantity'])
    value_in_cart = str(result['value'])
    return quantity_in_cart, value_in_cart  


    




