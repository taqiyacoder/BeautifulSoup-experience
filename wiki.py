import wikipedia as wiki

text = str(input("Enter:  "))

wiki_page = wiki.page(text)
print(F"{wiki_page.content}\n\n{wiki_page.url}")

wiki_pages = wiki.search(text)
for page in wiki_pages:
    if "novel" in page:
        print(page)
        wiki_page = wiki.page(page)
        br = wiki_page.content
        br = br.split("\n")[0]
        print(F"{br}\n\n{wiki_page.url}")


wiki_summary = wiki.summary(text)
print(wiki_summary)
        

from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.google.com/search?q=Book+named+{tex}")

soup = BeautifulSoup(r.text, 'html.parser')
specific_spans = soup.find('span', class_="hgKElc")


if specific_spans:
  text = specific_spans[0].text
  print(text)
else:
  print("No spans with class 'hgKElc' found")

import requests

def search_books(query):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "items" in data:
        for item in data["items"]:
            volume_info = item["volumeInfo"]
            title = volume_info.get("title", "No title available")
            authors = volume_info.get("authors", ["No author available"])
            publisher = volume_info.get("publisher", "No publisher available")
            published_date = volume_info.get("publishedDate", "No published date available")
            print("Title:", title)
            print("Authors:", ", ".join(authors))
            print("Publisher:", publisher)
            print("Published Date:", published_date)
            print("----")
    else:
        print("No books found matching the query.")

if __name__ == "__main__":
    query = input("Enter book title or author: ")
    search_books(query)