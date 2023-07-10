import requests
from bs4 import BeautifulSoup
r = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = r.text
soup = BeautifulSoup(data, "html.parser")
names = (soup.find_all(name = "h3", class_ = "title")).reverse()
for name in names:
    with open("movies.txt","a",encoding="utf-8") as movies:
        movies.write(name.text + "\n")
