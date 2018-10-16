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

try:
    bookmarkPath = '/home/shomick/projects/bookmarchive/bookmarks.json'
    with open(bookmarkPath) as jsonlocal:
        dictdump = json.loads(jsonlocal.read())
        print(dictdump)
except FileNotFoundError or json.JSONDecodeError:
        print("Improper JSON / File doesn't exist.")

    


