import requests
import json 

with open("config/finnhub_config.json") as f:
    config = json.load(f) 
    
API_KEY = config["api_key"]
SYMBOL = "APPL"
URL = f"https://finnhub.io/api/v1/quote?symbol={SYMBOL}&token={API_KEY}"

def extract_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Extracted Data: {data}")
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

if __name__ == "__main__":
    extract_data()
    