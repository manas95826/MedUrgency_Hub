import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
df = pd.read_csv('patient_activity.csv')

# Assuming the CSV has a column named 'Date' containing the visit dates
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

# Count the number of patient visits per month
monthly_counts = df['Month'].value_counts().sort_index()

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=monthly_counts.index, y=monthly_counts.values, palette='viridis')
plt.title('Patient Visits by Month')
plt.xlabel('Month')
plt.ylabel('Number of Visits')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

# Create a line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_counts.index, y=monthly_counts.values, marker='o')
plt.title('Patient Visits by Month')
plt.xlabel('Month')
plt.ylabel('Number of Visits')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.show()
