import json
import urllib.request, urllib.error
import ssl


URL_STRING = "http://py4e-data.dr-chuck.net/comments_1895399.json"
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
uh = urllib.request.urlopen(URL_STRING, context=ctx)
data = uh.read()
info = json.loads(data)
lst = info["comments"]
if lst is None or len(lst) == 0:
    raise LookupError("key comments doesn't exist")
s = 0
for item in lst:
    s = s + item["count"]
print(s)
