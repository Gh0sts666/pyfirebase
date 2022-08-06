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
	print("[ Error ] > Failed to import library")



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



# Main function
def main():
	"""
	Usage: python3 pyfirebase.py [-Option] [Argument]
	-h --help    For showing this help list
	-u --url     Firebase URL
	-b --brute   Bruteforce URL path
	-p --post    POST data
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", help="Firebase URL", required=True, dest="url")
	parser.add_argument("-b", "--brute", dest="txt_file")
	
	args    = parser.parse_args()
	URL     = args.url
	txtFile = args.txt_file
	
	if not URL.startswith("https"):
		echo("URL format must be in https!", red, bold)
		time.sleep(3)
		os.system("clear && python3 pyfirebase.py -h")
	elif not URL.__contains__("firebaseio.com"):
		echo("URL format must contain firebaseio.com", red, bold)
		time.sleep(3)
		os.system("clear && python3 pyfirebase.py -h")
	
	if txtFile.__contains__("/"):
		isDir = os.path.isdir(txtFile)
		if isDir:
			getLastPath = os.path.split(txtFile)
			print(getLastPath[1])
		else:
			echo("This is not a file!", red, bold)
	else:
		os.system("clear")
		with open(txtFile, 'r') as file:
			for data in file:
				URL = URL.replace(".json", "")
				url = URL + data + ".json"
				http = requests.get(url.strip())
				print(http.text)
				echo("Try: {}\n=>".format(data) + str(http.status_code) + "\n", green, bold)
			file.close()
				



if __name__ == '__main__':
	main()
