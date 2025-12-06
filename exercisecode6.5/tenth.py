# weather_snapshot.py
import requests
import json
import os
from datetime import datetime

# --- User Config ---
API_KEY = "799ac6831dda4e11a6c150122253010"   # Replace with your real WeatherAPI key
CITY = "Pondicherry"

# --- Folder & File Setup ---
today = datetime.now().strftime("%Y-%m-%d")
os.makedirs("snapshots", exist_ok=True)

success_file = f"snapshots/{today}.json"
error_file = f"snapshots/{today}.error.json"

# --- Weather API URL ---
url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

try:
    print(f" Fetching weather for {CITY}...")
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # raises error for 4xx / 5xx HTTP codes

    data = response.json()

    # Check if API returned an error structure
    if "error" in data:
        raise ValueError(data["error"]["message"])

    # Save successful snapshot
    with open(success_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f" Saved OK → {success_file}")

except requests.exceptions.Timeout:
    print("Request timed out.")
    with open(error_file, "w") as f:
        json.dump({"error": "timeout"}, f, indent=2)
    print(f"Saved error snapshot → {error_file}")

except requests.exceptions.RequestException as e:
    print("Network or API error:", e)
    with open(error_file, "w") as f:
        json.dump({"error": str(e)}, f, indent=2)
    print(f" Saved error snapshot → {error_file}")

except ValueError as e:
    print("API returned an error message:", e)
    with open(error_file, "w") as f:
        json.dump({"error": str(e)}, f, indent=2)
    print(f"Saved error snapshot → {error_file}")

except Exception as e:
    print("Unexpected error:", e)
    with open(error_file, "w") as f:
        json.dump({"error": "unexpected failure"}, f, indent=2)
    print(f"Saved error snapshot → {error_file}")
