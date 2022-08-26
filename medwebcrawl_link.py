import requests
import bs4 as bs 

link = "https://search.alexanderstreet.com/ctrn/browse/title"

data = requests.get(link).content

with open("alexander.html") as fp:
    soup = bs.BeautifulSoup(fp, 'html.parser')
    
filename= "links.txt"
links = []

for href in soup.find_all('a'):
    transcript = str(href.get('href'))
    if "/view/work/bibliographic_entity%7Cbibliographic_details" in transcript :
        if transcript not in links:
            links.append(transcript)
        

with open(filename, "a") as f:
    for i in links: 
        f.write(i + "\n")
    f.close()