import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Your API key (paste yours here)
API_KEY = "Replace with your actual API key"  # ⬅️ Replace with your actual API key
CITY = "Bengaluru"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Step 1: Get the data from API
response = requests.get(URL)
data = response.json()

# Step 2: Extract multiple types of data
dates = []
temperatures = []
humidity = []
wind_speed = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temperatures.append(entry['main']['temp'])
    humidity.append(entry['main']['humidity'])
    wind_speed.append(entry['wind']['speed'])

# Step 3: Create a dashboard with 3 charts
plt.figure(figsize=(14, 10))
sns.set_style("whitegrid")

# Chart 1: Temperature
plt.subplot(3, 1, 1)
sns.lineplot(x=dates, y=temperatures, marker='o', color='red')
plt.title(f"🌡️ Temperature Forecast for {CITY}")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Chart 2: Humidity
plt.subplot(3, 1, 2)
sns.lineplot(x=dates, y=humidity, marker='s', color='blue')
plt.title("💧 Humidity Forecast")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

# Chart 3: Wind Speed
plt.subplot(3, 1, 3)
sns.lineplot(x=dates, y=wind_speed, marker='^', color='green')
plt.title("🌬️ Wind Speed Forecast")
plt.ylabel("Wind Speed (m/s)")
plt.xlabel("Date and Time")
plt.xticks(rotation=45)

# Final Layout
plt.tight_layout()
plt.suptitle(f"📊 Weather Dashboard - {CITY}", fontsize=18, y=1.03)
plt.subplots_adjust(top=0.92)

# Show the dashboard
plt.show()
