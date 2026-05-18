from bs4 import BeautifulSoup

with open("sample.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())
# print(soup.title.string,type(soup.title.string))
# print(soup.div)
# print(soup.find_all("div")[1])

for link in soup.find_all("a"):
    print(link.get("href"))

s=soup.find(id="link3")
# print(s.get("href"))

# print(soup.find(class_="italic"))
# for child in soup.find(class_="container").children:
#     print(child)

# i=0
# for parent in soup.find(class_="box").parents:
#     i+=1
#     print(parent)
#     if(i==2):
#         break

# count= soup.find(class_="container")
# cont.name="span"
# print(cont)


# ulTag = soup.new_tag("ul")

# # First li tag
# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# # Second li tag
# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)

# # Insert into body
# soup.html.body.insert(0, ulTag)

# # Save modified HTML
# with open("modified.html", "w", encoding="utf-8") as f:
#     f.write(str(soup))


# cont=soup.find(class_="container")
# print(cont.has_attr("contenteditable"))

def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

results=soup.find_all(has_class_but_not_id)
print(results)