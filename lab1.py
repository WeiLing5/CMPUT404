import requests

response = requests.get("https://github.com/WeiLing5/CMPUT404/raw/master/lab1.py")

print response.text
