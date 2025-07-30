import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Delhi coordinates
latitude = 28.6519
longitude = 77.2315

# API endpoint (no API key needed!)
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

# Fetch data
response = requests.get(url)
data = response.json()

# Extract hourly temperature and timestamps
time_data = data['hourly']['time']
temperature_data = data['hourly']['temperature_2m']

# Convert string time to datetime objects
time_data = [datetime.fromisoformat(t) for t in time_data]

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(14, 6))
plt.plot(time_data, temperature_data, marker='o', linestyle='-', color='crimson')
plt.title("Hourly Temperature Forecast for Delhi", fontsize=16)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
