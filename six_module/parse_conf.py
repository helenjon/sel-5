import argparse
from ConfigParser import SafeConfigParser

class ParseConfig(object):
    def __init__(self):
        self.base_url = None
        self.file_name = None

#        self.parse_cli()  # This will parse the config file name from CLI
        self.parse_file() # This will parse the config file whose name you provide

#    def parse_cli(self):
#        parser = argparse.ArgumentParser(description="Parse conf file")
#        parser.add_argument("--conf", "-c", metavar="Conf", help="Config file name")
#        args = parser.parse_args()
#        self.file_name = args.conf

    def parse_file(self):
        parser = SafeConfigParser()
        parser.read('conf.ini')
        self.admin_url=parser.get('admin', 'admin_url')
        self.admin_login=parser.get('admin', 'admin_login')
        self.admin_password=parser.get('admin', 'admin_password')
        self.usstate=parser.get('section', 'usstate')
        self.postcodes=parser.get('section', 'postcodes')
        self.count_product=parser.get('section', 'count_product')
        self.list_of_titles=parser.get('section', 'list_of_titles')
    
    def parse_file_set(self, count_product=5):
        parser = SafeConfigParser()
        parser.read('conf.ini')
        parser.set('section', 'count_product', count_product)
        with open('conf.ini', 'w') as configfile:
                parser.write(configfile)



