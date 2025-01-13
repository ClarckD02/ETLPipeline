import requests
import json
import os

# Load API configuration
with open("config/Alpha_vantage_config.json") as f:
    config = json.load(f)

API_KEY = config["api_key"]
BASE_URL = config["base_url"]
SYMBOL = config["symbol"]

# Ensure the data directory exists
if not os.path.exists("data"):
    os.makedirs("data")

# Define the API endpoint for time series data
URL = f"{BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=5min&apikey={API_KEY}"

def extract_data():
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        if "Time Series (5min)" in data:
            print(f"Extracted Data: {list(data['Time Series (5min)'].keys())[:3]}...")  # Print first 3 timestamps for verification
            
            # Save data to JSON file
            with open("data/raw_stock_data.json", "w") as f:
                json.dump(data, f, indent=4)
            print("Data successfully saved to data/raw_stock_data.json")
            return data
        else:
            print(f"Error: {data}")  # Debugging unexpected responses
            return None
    else:
        print(f"Error fetching data: HTTP {response.status_code}")
        return None

if __name__ == "__main__":
    extract_data()



    