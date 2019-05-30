import pandas as pd
import requests, csv, json
from bs4 import BeautifulSoup
STATUS_CODE_OK = 200
URL = "https://nintypricer.com"

request = requests.get(URL)

if(request.status_code == STATUS_CODE_OK):
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find(name="table", attrs={'id':'datatable'})
    
    table_str = str(table)
    df = pd.read_html(table_str)[0]    
    # file = open("nintendo_switch_games_EUA.txt", "w")
    data = []
    for i in pd.read_html(table_str):
        for x in range (len(i.Title)):
            data.append({
                'game': i.Title[x].encode('utf-8'), 
                'price': i.eShopPrice[x]
            })
    
    with open('nintendo_switch_games_EUA.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)