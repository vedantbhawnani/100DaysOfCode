from bs4 import BeautifulSoup
import requests

article_data = []
article_link = []

r = requests.get("https://news.ycombinator.com/")
data = r.text

soup = BeautifulSoup(data, "html.parser")
links_data = soup.find_all(class_ = "titleline")

for i in range(len(links_data)):
    article_data.append(links_data[i].a.text)
    article_link.append(links_data[i].a.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = 'span', class_ = "score")]

# zipped = zip(article_upvotes, article_data, article_link)
# sorted(zipped)

article_upvotes, article_data, article_link = zip(*sorted(zip(article_upvotes, article_data, article_link),reverse=True))
print(article_data)
print(article_link)
print(article_upvotes)

