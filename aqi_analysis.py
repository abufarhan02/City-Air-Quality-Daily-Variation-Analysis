import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Get base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct paths
data_path = os.path.join(BASE_DIR, "data", "aqi_data.csv")
output_path = os.path.join(BASE_DIR, "visuals", "daily_variation.png")

# Load dataset
data = pd.read_csv(data_path)

# Descriptive statistics
mean_aqi = data['AQI'].mean()
median_aqi = data['AQI'].median()
std_dev = data['AQI'].std()
max_aqi = data['AQI'].max()

# Peak pollution hour
peak_hour = data.loc[data['AQI'].idxmax(), 'Hour']

print("\nDescriptive Statistics")
print("----------------------")
print(f"Mean AQI: {mean_aqi:.2f}")
print(f"Median AQI: {median_aqi:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Maximum AQI: {max_aqi}")
print(f"Peak Pollution Hour: {peak_hour}")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(data['Hour'], data['AQI'], marker='o')
plt.title("Daily AQI Variation")
plt.xlabel("Hour of Day")
plt.ylabel("AQI")
plt.grid(True)

# Save and show
plt.savefig(output_path)
plt.show()
