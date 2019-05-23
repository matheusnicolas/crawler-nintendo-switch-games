# -*- coding: utf-8 -*-
import json

with open("nintendo.json") as json_file:
    data = json.load(json_file)
    for i in data['results']:
        for j in i['hits']:
            #print(j['title'])
            print("Game: {} - Price: {}".format(j['title'], j['msrp']))

