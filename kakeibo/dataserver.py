import requests
url = 'http://127.0.0.1:49379'
response = requests.get(url)
print(response)
print(type(response))