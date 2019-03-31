import requests

def get_request(url):
    value = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename,'wb') as objec:
        objec.write(value.content)

get_request(input("url>> "))
