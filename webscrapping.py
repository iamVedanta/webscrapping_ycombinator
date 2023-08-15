from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

tag = soup.find_all(name="a",class_="hnuser")

tag_link = soup.find_all(name="span", class_="titleline")
print(tag_link)


article_upvote = soup.find_all(name="span", class_="score")
article_links=[]
for i in tag_link:
    article_link = i.find(name="a").get('href')
    article_links.append(article_link)

arrange = zip(tag,article_upvote,article_links)
arranged = []
for x,y,z in arrange:
    arranged.append((x.getText(),int(y.getText().split(" ")[0]),z))

answer = sorted(arranged,key=lambda x:x[1], reverse=True)
print(answer)

for j in answer:
    print(j)

print()
print("The most popular article is ",answer[0])