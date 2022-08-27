from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, strftime, time

url_links = "https://search.alexanderstreet.com/ctrn/browse/title"
url_login = "https://search.alexanderstreet.com/user"

usern = "ymw200000@utdallas.edu"
pw = "00000000"

links=[]

# Define Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Create new automated instance of Brave
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#login
driver.get(url_login)

#enter user
user_in = driver.find_element("id",'edit-name')
user_in.send_keys(usern)

#enter pass
user_pass = driver.find_element("id",'edit-pass')
user_pass.send_keys(pw)

#submit
driver.find_element("id",'edit-submit').click()

sleep(1)

#go to links page
driver.get(url_links)

sleep(3)

results = driver.find_elements("class name", 'search-result-item-info columns large-12 medium-12' )


for result in results:
    links.append(str(result.find_elements("xpath","//a[@href]")))

print(links[0])

sleep(2)



