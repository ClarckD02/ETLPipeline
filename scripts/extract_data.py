import requests
import json

# Load API key and config from JSON
with open("config/alpha_vantage_config.json") as f:
    config = json.load(f)

API_KEY = config["api_key"]
BASE_URL = config["base_url"]
SYMBOL = config["symbol"]

# Construct the API request URL for stock time series
URL = f"{BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=5min&apikey={API_KEY}"

def extract_stock_data():
    """Extract stock data from Alpha Vantage API."""
    print(f"Requesting data from: {URL}")
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        print(f"Extracted Data: {json.dumps(data, indent=4)}")

        # Save extracted data as JSON
        with open("data/raw_stock_data.json", "w") as f:
            json.dump(data, f, indent=4)

        return data
    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    extract_stock_data()

    