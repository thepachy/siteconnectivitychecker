import requests

f = open('result.txt', 'tw', encoding = 'utf-8')

def SCC(url):
    global f
    try:
        requests.get(url)
        f.write("The connection is excellent")
        #f.close()
    except requests.ConnectionError as err:
        f.write("No connection")
        #f.close()

url = input("Enter website url: ")
SCC(url)
f.close()