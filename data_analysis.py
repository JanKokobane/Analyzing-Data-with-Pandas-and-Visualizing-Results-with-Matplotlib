# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -----------------------------
# Task 1: Load and Explore the Dataset
# -----------------------------

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target  # Add target column
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})  # Map target to species names

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values (if any)
# Uncomment if needed: df.fillna(method='ffill', inplace=True) or df.dropna(inplace=True)

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------

# Compute basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Group by 'species' and compute the mean of each group
grouped = df.groupby('species').mean()
print("\nMean values by species:")
print(grouped)

# -----------------------------
# Task 3: Data Visualization
# -----------------------------

# 1. Line Chart: Trends Over Time (simulating time-series trends with indices)
plt.figure(figsize=(10, 5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.plot(subset.index, subset['sepal length (cm)'], label=species)

plt.title('Trends in Sepal Length Over Indices')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# 2. Bar Chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='species', y='petal length (cm)', ci=None, palette='viridis')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal width (cm)'], bins=20, kde=True, color='orange')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', style='species', palette='deep')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# -----------------------------
# Error Handling Example (For CSV loading)
# -----------------------------

try:
    # Example: Replace 'your_dataset.csv' with the path to your dataset file
    df = pd.read_csv(r'C:\Users\John\Desktop\gsalc.csv')  
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An error occurred: {e}")
