import urllib.request
import xml.etree.ElementTree as ElementTree

url = "https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US"
req = urllib.request.urlopen(url)
page=req.read()
doc = ElementTree.fromstring(page)

for item in doc.iter('item'):
    title = item.find('title').text
    print("---")
    pubDate = item.find('pubDate').text
    print(pubDate.strip())
    print(title.strip())
    description = item.find('description').text
    print(description.strip())
    link = item.find('link').text
    print(link.strip())
