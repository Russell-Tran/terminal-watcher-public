from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import json
import unicodedata
import csv

### TODO:
# 0) Load Trouble Check information
# 1) Make sure code works for multiple-container input and for all containers
# 2) Make each click/page load robust with WebDriverWait and error messages
# 3) Reconfigure code to take in username and desired container(s) as program input
# 4) Modify output format as desired / write to database as necessary
###################################################################################

opts = Options()

#opts.set_headless()
#assert opts.headless  # Uncomment these two lines to operate in headless mode

browser = Firefox(options=opts)
finished = 0
while finished == 0:
	try:
		browser.get('https://www.ttilgb.com/main/index.do')
		finished = 1
	except:
		sleep(2)

sleep(2)

username = browser.find_element_by_id("pUsrId")
password = browser.find_element_by_id('pUsrPwd')
username.send_keys('B86569') # yourusername
password.send_keys('coffee1') # yourpassword

#Log in
browser.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/img").click()

#Container Input Page
sleep(2)
browser.get('https://www.ttilgb.com/uiArp01Action/openScreen.do')

sleep(2)
cinput = browser.find_element_by_id("cntrNos")
cinput.send_keys(Keys.TAB)
cinput.clear()
cinput.send_keys("BEAU2820198")

#Submit container query
browser.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[3]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/a").click()

#Scrape container information from table
sleep(2)
contdata = browser.find_element_by_id("grid1")
htmltable = contdata.get_attribute("outerHTML")

soup = BeautifulSoup(htmltable, 'html.parser')
table_data = [[unicodedata.normalize("NFKD", cell.text) for cell in row("td")] for row in soup("tr")]
print(table_data)

#First row is all empty strings
del table_data[0]

#I assume table_headers are fixed, no matter the container
table_headers = ["", "Container No", "Available for Pickup", "TMF", "Rail", "Trouble Check", "Appt Time", "Yard Location", "Hold Reason", "Customs Status", "Freight Status", "USDA Status", "Carrier Status", "Terminal Status", "Demurrage Due?", "Deumurrage Amount", "Last Free Day", "Paid Through Date", "SSCO", "SCAC", "Container Type/Length/Height"]  


#Write output to csv
with open("output.csv",'w') as resultFile:
    wr = csv.writer(resultFile)
    wr.writerow(table_headers)
    wr.writerows(table_data)

#Note: The last four columns of table_data seem to be hidden when viewing the website,
#so ignore 'SSCO HOLD', 'TERMINAL HOLD ', ' ', 'Inbond'
#when working with output csv file.