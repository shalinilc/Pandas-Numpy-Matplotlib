import pandas as pd
import numpy as np

file_path = "C:/Users/shali/Desktop/ai nu tech/1-Assessnment/archive/WineQT.csv"
data = pd.read_csv(file_path)

# Assuming 'df' is your DataFrame with 'alcohol', 'pH', and 'citric acid' columns
columns = ['alcohol', 'pH', 'citric acid']

# Loop through each column and calculate the statistics
for column in columns:
    print(f"Statistics for {column}:")
    print(f"Mean: {np.mean(data[column])}")
    print(f"Median: {np.median(data[column])}")
    print(f"Standard Deviation: {np.std(data[column])}")
    print(f"Minimum: {np.min(data[column])}")
    print(f"Maximum: {np.max(data[column])}")
    print()  # Blank line for separation between columns

#corellation
correlation_alcohol_quality = np.corrcoef(data['alcohol'], data['quality'])[0, 1]
print(f"Correlation between alcohol and quality: {correlation_alcohol_quality}")

correlation_sugar_quality = np.corrcoef(data['residual sugar'], data['quality'])[0, 1]
print(f"Correlation between residual sugar and quality: {correlation_sugar_quality}")

#arrays
alcohol_array = data['alcohol'].to_numpy()
pH_array = data['pH'].to_numpy()

# Normalize the 'alcohol' column
alcohol_normalized = (alcohol_array - np.min(alcohol_array)) / (np.max(alcohol_array) - np.min(alcohol_array))
print(f"Normalized alcohol values:\n{alcohol_normalized}")

# Normalize the 'pH' column
pH_normalized = (pH_array - np.min(pH_array)) / (np.max(pH_array) - np.min(pH_array))
print(f"Normalized pH values:\n{pH_normalized}")

#statastical analysis
data['alcohol_quality'] = data['alcohol'].apply(lambda x: 'High Quality' if x > 7 else 'Low Quality')
print(data[['alcohol','alcohol_quality']])