import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import time
import random

class Extractor():   
    def get_links(self, url):
        http = httplib2.Http()
        response, content = http.request(url, headers={'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'})
        links=[]
        for link in BeautifulSoup(content).find_all('a', href=True):
            links.append(link['href'])  
        return links

f = open("outputfile.txt", "w")
for i in range(1, 1116):
    print(f"Strona: {i}")
    url = "https://SOMEWEBSITE/" + str(i) + "/"
    myextractor = Extractor()
    links = myextractor.get_links(url)
    for link in links:
        if 'CHECK CONDITION ON WEBPAGE' in link:
            print(f"https://SOMEWEBSITE/{link}")
            f.write(f"https://SOMEWEBSITE/{link}\n")
    time.sleep(random.randint(1,10))
f.close()
