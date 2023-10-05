import urllib.request as request
import bs4
import ssl

# Supress ssl certification errors
contex = ssl.create_default_context()
contex.check_hostname = False
contex.verify_mode = ssl.CERT_NONE

URL_STRING = "http://py4e-data.dr-chuck.net/comments_1895396.html"
parsed_html = bs4.BeautifulSoup(request.urlopen(URL_STRING), "html.parser")
comments_count_list = parsed_html("span")

comments_sum = 0
for row in comments_count_list:
    comments_sum = comments_sum + int(row.text)
print(comments_sum)