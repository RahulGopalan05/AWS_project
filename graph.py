import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv(r'C:\Users\rahul\Downloads\weather.csv')  # Replace 'your_data.csv' with the actual CSV file path

# Create a histogram for Rainfall
plt.figure(figsize=(8, 6))
plt.hist(df['Rainfall'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Rainfall')
plt.xlabel('Rainfall')
plt.ylabel('Frequency')
plt.show()

# Create a scatter plot for Temperature
plt.figure(figsize=(8, 6))
plt.scatter(df['MaxTemp'], df['MinTemp'], color='green', alpha=0.5)
plt.title('Scatter Plot of MaxTemp vs. MinTemp')
plt.xlabel('MaxTemp')
plt.ylabel('MinTemp')
plt.grid(True)
plt.show()

# Create a bar chart for RainTomorrow
rain_tomorrow_counts = df['RainTomorrow'].value_counts()
plt.figure(figsize=(6, 4))
rain_tomorrow_counts.plot(kind='bar', color='lightblue')
plt.title('Count of RainTomorrow (Yes/No)')
plt.xlabel('RainTomorrow')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
