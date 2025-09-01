import requests
import csv

# API endpoint and credentials
url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"
headers = {
    "X-RapidAPI-Key": "879fe1fcf6msh330f7cc00abbf03p1c14dejsn9ef1bf472f19",  # Your API key
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}
params = {
    "formatType": "odi"  # Change to 'odi' or 't20' if needed
}

# Make API call
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    # Extract 'rank' data from JSON response
    data = response.json().get("rank", [])
    csv_filename = "test_batsmen_rankings.csv"

    if data:
        field_names = ["rank", "name", "country"]

        # Write extracted data to CSV
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()  # Write CSV headers
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"✅ Data fetched successfully and saved to '{csv_filename}'")
    else:
        print("⚠️ No ranking data found in API response.")
else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")
