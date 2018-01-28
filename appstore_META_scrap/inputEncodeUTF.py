#!/usr/bin/env python3

import sys
import urllib.parse as parse

if len(sys.argv) <= 1:
	print("input any string")
	sys.exit()
input = sys.argv[1]

baseUrl = "https://play.google.com"
searchUrl = "/store/search?"

params = {
	'q': input
}

encodedText = parse.urlencode(params)
print("Input text : ", input)
print("Encoded text : ", encodedText)

targetUrl = baseUrl + searchUrl + encodedText + "&c=apps"
print("Target URL : ", targetUrl)