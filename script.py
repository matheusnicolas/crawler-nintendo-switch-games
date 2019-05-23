import pandas as pd
import requests
from bs4 import BeautifulSoup
STATUS_CODE_OK = 200

request = requests.get("https://nintypricer.com/")

if(request.status_code == STATUS_CODE_OK):
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find(name="table")
    
    table_str = str(table)
    df = pd.read_html(table_str)[0]
    print(df)