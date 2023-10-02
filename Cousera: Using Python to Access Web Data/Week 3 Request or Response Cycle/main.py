import requests
request = requests.get("http://data.pr4e.org/intro-short.txt")
headers = dict(request.headers)
print(headers)
print(request)
