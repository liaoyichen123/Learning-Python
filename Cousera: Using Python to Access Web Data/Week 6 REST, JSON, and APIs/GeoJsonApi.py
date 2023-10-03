import urllib.request, urllib.parse, urllib.error
import json
import ssl
from types import SimpleNamespace

API_KEY = 42
SERVICE_URL = 'http://py4e-data.dr-chuck.net/json?'
ADDRESS_STRING = 'universidad complutense de madrid'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# http://py4e-data.dr-chuck.net/json?


address = ADDRESS_STRING
parms = dict()
parms['address'] = address
if API_KEY is not False: parms['key'] = API_KEY
url = SERVICE_URL + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

print(json.dumps(js, indent=4))

lat = js['results'][0]['geometry']['location']['lat']
lng = js['results'][0]['geometry']['location']['lng']
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)
