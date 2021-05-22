import requests
from time import sleep

f = open('result_scc.txt', 'tw', encoding = 'utf-8')

def siteconnectivitychecker(url, count, time):
	global f
	i = 1
	while i <= count:
		try:
			requests.get(url)
			f.write("The connection to " + url + " is excellent, Attempt: " + str(i) + "\n")
			print("Attempt:", i)
			if i != count:
				sleep(time)
			i += 1
		except requests.ConnectionError as err:
			f.write("No connection to " + url + ", Attempt: " + str(i) + "\n")
			print("Attempt:", i)
			if i != count:
				sleep(time)
			i += 1

url = input("Enter website url: ")
count = int(input("Enter the number of attempts: "))
time = float(input("Enter the delay in seconds: "))
siteconnectivitychecker(url, count, time)
f.close()