import urllib.request
import xml.dom.minidom
file1 = urllib.request.urlopen('https://www.moea.gov.tw/MNS/populace/news/NewsRSSdetail.aspx?Kind=1')
DOMTree = xml.dom.minidom.parse(file1)
file1.close()

type(DOMTree)
collection = DOMTree.documentElement
if collection.hasAttribute("schemaLocation"):
    print(f'schemaLocation={collection.getAttribute("schemaLocation")}')

items = collection.getElementsByTagName("item")
for item in items:
    title = item.getElementsByTagName('link')
    print(title[0].childNodes[0].data)
    description = item.getElementsByTagName('description')

