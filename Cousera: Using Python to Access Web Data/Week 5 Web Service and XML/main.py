import ssl
import urllib.request
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
URL_STRING = "http://py4e-data.dr-chuck.net/comments_1895398.xml"
uh = urllib.request.urlopen(URL_STRING, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall("./comments/comment/count")
s = 0
for item in lst:
    s = s + int(item.text)
print(s)


