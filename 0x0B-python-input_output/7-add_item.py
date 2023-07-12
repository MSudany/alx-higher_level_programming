#!/usr/bin/python3
'''py script'''


import json
import sys
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


myList = []
for arg in sys.argv[1:]:
    myList.append(arg)

save_to_json_file(myList, 'add_item.json')
load_from_json_file('add_item.json')
