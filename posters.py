from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import sqlite3
import time
import wikipedia

dbfile = ""
connection = sqlite3.connect(dbfile)
cursor = connection.cursor()
cursor.execute('SELECT * FROM movies')
items = cursor.fetchall()
connection.commit()
connection.close()

base = ""

for item in items:
    name = item[0].lower().replace(" ", "+")
    time.sleep(1)
    
    result = wikipedia.search(name+" (film)")
    url = base.replace("en.","en.m.")+"/wiki/" + result[0].replace(" ",  "_")
    page = urlopen(url.replace("\u2013", "-"))
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    images = soup.find_all("img")
    source = images[1]['src']

    response = requests.get("https:"+source)
    file = open(name+".png","wb")
    file.write(response.content)
    file.close()