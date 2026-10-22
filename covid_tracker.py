"""Option 2: COVID-19 Data Tracker
Dataset: 
COVID-19 Dataset (Our World in Data)
Tasks:
● Load data using Pandas
● Display top 5 countries by total cases
● Plot bar chart (Matplotlib)
Skill Gain: Data visualization + analysis"""


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
url = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
df = pd.read_csv(url)

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Check required columns
print("\nAvailable columns:")
print(df.columns.tolist())

# Select the required columns
data = df[["country", "date", "total_cases"]].copy()

# Convert columns into suitable formats
data["date"] = pd.to_datetime(data["date"], errors="coerce")
data["total_cases"] = pd.to_numeric(data["total_cases"], errors="coerce")

# Remove rows with missing values
data = data.dropna(subset=["country", "date", "total_cases"])

# Get the latest record for each country
latest = (data.sort_values("date").groupby("country").tail(1))

# Exclude continents and other regional aggregates
latest = latest[~latest["country"].isin([
        "World", "Africa", "Asia", "Europe",
        "North America", "South America",
        "Oceania", "European Union"])]

# Find the top 5 countries
top5 = latest.nlargest(5, "total_cases")

print("\nTop 5 countries by total COVID-19 cases:")
print(top5[["country", "total_cases"]].to_string(index=False))

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(top5["country"], top5["total_cases"])

plt.title("Top 5 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=30)
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()

# Save and display chart
plt.savefig("covid_top5_bar_chart.png")
plt.show()

