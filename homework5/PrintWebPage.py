import requests
page = requests.get('http://www.baidu.com').content
print(page)
