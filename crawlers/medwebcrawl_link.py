from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import json

target = input('Enter target: ')
auth_ = input('auth required?(y/n): ')
isUTD = input("is utd?(y/n): ")
isDL = input("is it a download?(y/n): ")
utdJSON_path ='crawlers/elems_JSON/utd_els.json'
elemsJSON_path ='crawlers/elems_JSON/elems.json'

with open(utdJSON_path, "r") as j:
    utd_els = json.loads(j.read())
    
with open(elemsJSON_path, "r") as j:
    elems = json.loads(j.read())

links = []

# Define Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser-Nightly/Application/brave.exe"
options = webdriver.ChromeOptions()
options.binary_location = brave_path

#set dl options
prefs = {"download.default_directory" : "C:/Users/thewa/Desktop/projects/computational_neuroscience/AI_ML/projects/mun_ching/crawlers/content", "download.prompt_for_download" : False}

options.add_experimental_option("prefs",prefs)

# Create new automated instance of Brave
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)



def auth():

    url_login = elems["url"]
    # login
    if isUTD != 'y':

        driver.get(url_login)
        usern = elems["user"]
        pw = input("Enter pass:")
        user_in = driver.find_element("id", elems["u_el"])
        user_in.send_keys(usern)

    # enter pass   
        user_pass = driver.find_element("id", elems["p_el"])
        user_pass.send_keys(pw)

        # submit
        driver.find_element("id", elems["sub_el"]).click()

    else:

        driver.get(target)
        #user
        usern=utd_els["user"]
        user_in = driver.find_element("id", utd_els["u_el"])
        user_in.send_keys(usern)
        #pass
        sleep(1)
        pw = input("Enter pass:")
        user_pass = driver.find_element("id", utd_els["p_el"])
        user_pass.send_keys(pw)
        #submit
        driver.find_element("id", utd_els["sub_el"]).click()

        sleep(1)

def getLinks():

    link_el = [input("Paste the element type that has the links if class, class name , if id, id, if name, name, etc: "), input(
            "Paste that elements name:")]



    with open('crawlers/links.txt', "w") as l:

        results = driver.find_element(link_el[0],link_el[1])
        links = results.find_elements("xpath","a[@target='blank']")

        for link in links:
            if isDL == 'y':
                link.click()
            l.write(link.get_attribute("href") + '\n')
            sleep(1)

    sleep(2)        
       

if __name__ == '__main__':
    #check if auth is required
    if auth_ == 'y':
        auth()

    driver.get(target)

    getLinks()

    
    

    
    
