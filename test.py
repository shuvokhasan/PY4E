import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

data = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1796666.xml').read()
xml_data = ET.fromstring(data)
search_str = "comments/comment"
count_tags = xml_data.findall(search_str)

total=0
for tags in count_tags:
    c=tags.find('count')
    total+=int(c.text)
    
print(total)