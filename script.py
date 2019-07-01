import pandas as pd
import requests, csv, json
from bs4 import BeautifulSoup
STATUS_CODE_OK = 200
URL = "https://nintypricer.com/" # => "https://nintypricer.com/{region}"
REGIONS = ["at", "au", "be", "bg", "ca", "ch", "cy", "cz", "de", "dk",
            "ee", "es", "fi", "fr", "gb", "gr", "hr", "hu", "ie", "it",
            "lt", "lu", "lv", "mt", "mx", "nl", "no", "nz", "pl", "pt",
            "ro", "ru", "se", "si", "sk", "za"]
JSON_NAME = "nintendo_switch_games_EUA.json"

request = requests.get(URL)

def extract_page():
    if(request.status_code == STATUS_CODE_OK):
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find(name="table", attrs={'id':'datatable'})
        table_str = str(table)
    return table_str

def populate_json(table_str):
    data = []
    pd.read_html(table_str)[0]
    for i in pd.read_html(table_str):
        for x in range (len(i.Title)):
            data.append({
                'game': i.Title[x].encode('utf-8'), 
                'price': i.eShopPrice[x]
            })
    return data

def output_json(data):
    with open(JSON_NAME, 'w') as outfile:
        json.dump(data, outfile, indent=2)

html = extract_page()
data = populate_json(html)
output_json(data)