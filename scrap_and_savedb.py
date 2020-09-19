import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import MySQLdb

#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "root"
PASSWORD = "root"
DATABASE = "scrapdata"

driver=webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get("https://www.cpppc.org:8082/inforpublic/homepage.html#/projectDetail/91fe736c280a47b183e2727b40cc8dc4")
res=driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup=BeautifulSoup(res,'lxml')
box=soup.find('div',{'id':"combineStagePrepare"})
all_hack=box.find_all('div',{'class':'publicWrapper'})
for x in all_hack:
    h_type=x.find('p',{'class':'title'}).text
    tab=x.find('table',{'class':'viewTable'}).text
    #print(h_type,tab)
from googletrans import Translator
trans=Translator()
t=trans.translate(h_type)
y=trans.translate((tab))
print(t.text)
print('\n')
print(y.text)

# Open database connection
db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)

# prepare a cursor object using cursor() method
cursor = db.cursor()
sql="INSERT INTO table (t,y) VALUES (%s, %s)"
try:
 # Execute the SQL command
 cursor.execute(sql,
                (
                    item.get("t.text"),
                    item.get("y.text"),
                )
               )
 # Commit your changes in the database
 db.commit()
except:
 # Rollback in case there is any error
 db.rollback()
 # disconnect from server
 db.close()