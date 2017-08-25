import configargparse

'''
Reads file variables and assigns them to Python variables for
further use
'''
#Create a parser instance. 
#ini file should be in the same folder
p = configargparse.ArgParser(default_config_files=['options.ini'])

#Read variables by name(key):
#'--key' to show its name in file, dest="key" to store it in code

p.add_argument("--usstate", dest="usstate")
p.add_argument("--postcodes", dest="postcodes")

args = p.parse_args()

#Create new product > ProductGroups> value

ticket estimation, grooming

update regression test plan 