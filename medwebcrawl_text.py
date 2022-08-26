from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs

url = "https://search.alexanderstreet.com/ctrn/browse/title"

# Define Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Create new automated instance of Brave
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#links array
links = []

#get links
with open("links.txt","r") as f:
    links = f.readlines()

#strip '\n'
for i in range(0,len(links)):
    links[i] = links[i].strip('\n')

#url = url + links[0]
url = "https://search.alexanderstreet.com/view/work/bibliographic_entity%7Cbibliographic_details%7C2107288/client-session-november-16-2012-client-concerned-about-managing-his-anxieties-and-occupational"

#get page
driver.get(url)

#test: print source
html = driver.page_source


print(url + '\n')
print(html)