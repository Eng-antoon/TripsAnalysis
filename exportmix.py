import requests
import datetime
import pandas as pd
import json

# Configuration: Replace with your Mixpanel API secret
API_SECRET = '725fc2ea9f36a4b3aec9dcbf1b56556d'
EVENT_NAME = "trip_details_route"

# Calculate the date range for the past 10 days
today = datetime.date.today()
ten_days_ago = today - datetime.timedelta(days=8)
from_date = ten_days_ago.strftime('%Y-%m-%d')
to_date = today.strftime('%Y-%m-%d')

# Mixpanel Export API endpoint
url = "https://data.mixpanel.com/api/2.0/export/"

# Query parameters for the API request
params = {
    'from_date': from_date,
    'to_date': to_date,
    'event': f'["{EVENT_NAME}"]'
}

# Headers: specify that we accept JSON
headers = {
    'Accept': 'application/json'
}

# Execute the GET request with HTTP Basic Authentication
response = requests.get(url, auth=(API_SECRET, ''), params=params, headers=headers)

if response.status_code == 200:
    records = []
    # Process each newline-delimited JSON record
    for line in response.text.strip().splitlines():
        if line:
            record = json.loads(line)
            # Flatten the JSON: take all keys from "properties" and add the "event" key if needed.
            if 'properties' in record:
                data = record['properties']
                # Optionally include the event name (if you want this column in your Excel)
                data['event'] = record.get('event', None)
            else:
                data = record
            records.append(data)
    
    # Create a DataFrame with all records
    df = pd.DataFrame(records)
    
    # Adjust column headers: remove any leading '$' characters
    df.rename(columns=lambda x: x.lstrip('$'), inplace=True)
    
    # Convert the 'time' column from Unix timestamp (seconds) to human-readable dates if present
    if 'time' in df.columns:
        df['time'] = pd.to_datetime(df['time'], unit='s')
    
    # Convert the 'mp_api_timestamp_ms' column from Unix timestamp in milliseconds to human-readable dates if present
    if 'mp_api_timestamp_ms' in df.columns:
        df['mp_api_timestamp_ms'] = pd.to_datetime(df['mp_api_timestamp_ms'], unit='ms')
    
    # Save the entire DataFrame to an Excel file
    excel_file = 'mixpanel_export.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"Data successfully saved to {excel_file}")
else:
    print("Failed to export data:", response.status_code, response.text)
