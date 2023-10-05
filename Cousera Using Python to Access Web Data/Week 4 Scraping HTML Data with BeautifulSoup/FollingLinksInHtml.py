import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

URL_STRING = "http://py4e-data.dr-chuck.net/known_by_Teejay.html"
COUNT_INT = 7
POSITION_INT = 18

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# click and print out text field at X position for N times
def print_name(url, position, counter):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = list(soup('a'))
    counter = counter - 1
    print(tags[position - 1].text)
    if counter > 0:
        print_name(tags[position - 1].get("href", None), position, counter)
    else:
        return


print_name(URL_STRING, POSITION_INT, COUNT_INT)
