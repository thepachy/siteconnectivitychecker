import requests

def SCC(url):
    try:
        requests.get(url)
        print("The connection is excellent")
    except requests.ConnectionError as err:
        print("No connection")

url = input("Введите адрес сайта: ")
SCC(url)