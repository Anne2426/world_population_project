
# world_population_analytics.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("world_population.csv")  # Ensure this file is in the same folder

# Basic inspection
print("First 5 rows of the dataset:")
print(df.head())

# Top 10 most populous countries in 2020
top10_2020 = df[df['Year'] == 2020].sort_values(by='Population', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='Population', data=top10_2020, palette='viridis')
plt.xticks(rotation=45)
plt.title('Top 10 Most Populous Countries in 2020')
plt.tight_layout()
plt.savefig("top10_populous_2020.png")
plt.show()

# Population growth of India over time
india_data = df[df['Country'] == 'India']

plt.figure(figsize=(10, 5))
plt.plot(india_data['Year'], india_data['Population'], marker='o', color='green')
plt.title('India Population Growth Over Time')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.tight_layout()
plt.savefig("india_population_growth.png")
plt.show()
