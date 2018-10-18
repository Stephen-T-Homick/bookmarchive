#!/usr/bin/python3
'''
TODO:

* Define path of json file
* Get json stored in an object as a type 'dict' 
* Convert that file with json2html library to an html file and truncate / write that result to a new file
'''

import json
import sys
from json2html import *
from time import sleep
from bs4 import BeautifulSoup

bookmarkPath = '/home/shomick/projects/bookmarchive/Bookmarks.json'
with open('/home/shomick/projects/bookmarchive/Bookmarks.json') as jsonfile:
    parsed = json.load(jsonfile)    
    html_doc = json2html.convert(json = parsed)
    #print(json.dumps(parsed,indent=2,sort_keys=True)) #Print pretty JSON
    #print(json2html.convert(json = parsed)) #Print json -> html 
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())
    
    


