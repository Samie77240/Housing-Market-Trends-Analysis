
import pandas as pd

# Load the dataset
file_path = 'housing[1].csv'
housing_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(housing_data.head())

# Calculate summary statistics
summary_stats = housing_data.describe()
print("\nSummary Statistics:")
print(summary_stats)

# Save summary statistics to a CSV file
summary_stats.to_csv('summary_statistics.csv')
