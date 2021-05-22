import requests

f = open('result.txt', 'tw', encoding = 'utf-8')

def SCC(url, times):
    global f
    i = 1
    while i <= times:
    	try:
        	requests.get(url)
        	f.write("The connection is excellent, Attempt: " + str(i) + "\n")
        	print("Attempt:", i)
        	i += 1
    	except requests.ConnectionError as err:
        	f.write("No connection, Attempt: " + str(i) + "\n")
        	print("Attempt:", i)
        	i += 1

url = input("Enter website url: ")
times = int(input("Enter the number of attempts: "))
SCC(url, times)
f.close()