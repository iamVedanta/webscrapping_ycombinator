from bs4 import BeautifulSoup
#import lxml -- use this if html.paarser doesnt work


file = open(r"C:\Users\h\Downloads\bs4-start\website.html", encoding="utf8")
contents = file.read()

soup = BeautifulSoup(contents,'html.parser')

print(soup.title)
#print(soup.prettify()) -- gives only the first component

print(soup.a)

all_anchor_= soup.find_all(name='a') #returns all the tags in the form of a list
print(all_anchor_)

for tag in all_anchor_:
    #print(tag.string)
    #print(tag.getText())
    print(tag.get('href'))

print()
heading = soup.find(name='h1', id='mynames')
print(heading)

section_heading=soup.find(name="h3", class_='heading')
print(section_heading.getText())

name = soup.select_one(selector="#myname") #-- for id use #
print(name)

headings = soup.select(selector=".heading") #-- for class use dot(.)
print(headings)