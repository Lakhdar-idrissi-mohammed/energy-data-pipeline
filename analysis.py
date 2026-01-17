import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
print("Loading data...")
df = pd.read_csv('meter_data.csv')

# 2. Clean Data
df['Date'] = pd.to_datetime(df['Date'])
df = df.drop_duplicates() # Remove that duplicate row
df['Consumption_kWh'] = df['Consumption_kWh'].fillna(df['Consumption_kWh'].mean()) # Fix missing value

# 3. Save for Power BI
df.to_csv('cleaned_data.csv', index=False)
print("Success! cleaned_data.csv created.")

# 4. Generate a quick chart (The "Visual" Bonus)
daily_total = df.groupby('Date')['Consumption_kWh'].sum()
daily_total.plot(kind='bar', color='orange')
plt.title('Daily Energy Consumption')
plt.savefig('energy_chart.png')
print("Chart saved as energy_chart.png")