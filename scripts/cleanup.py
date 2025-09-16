import pandas as pd
import numpy as np

# Load the raw data
print("Loading data from Excel file...")
data = pd.read_excel("../data/raw/messy_supermarket_sales.xlsx")

# Show basic statistics
print("\nData Description:")
print(data.describe(include='all'))

# Show info about data types and missing values
print("\nData Info:")
print(data.info())

# Show a random sample of 10 rows
print("\nSample of 10 rows:")
print(data.sample(10))

# Standardize Store_Location values
print("\nUnique Store_Location values before cleanup:")
print(data.Store_Location.unique())
data.replace({"Store_Location": {"Online": "Online", "Suburb": "Physical", "Downtown": "Physical", "Mall": "Physical"}}, inplace=True)
print("Unique Store_Location values after cleanup:")
print(data.Store_Location.unique())

# Drop rows with missing Customer_ID (likely walk-ins)
print("\nDropping rows with missing Customer_ID...")
data.dropna(subset=["Customer_ID"], inplace=True)

# Drop any remaining rows with missing data
print("Dropping any remaining rows with missing values...")
data.dropna(inplace=True)

# Convert Date column to datetime
print("Converting 'Date' column to datetime...")
data["Date"] = pd.to_datetime(data["Date"], errors='coerce')

# Drop duplicate rows
print("Dropping duplicate rows...")
data.drop_duplicates(inplace=True)

# Calculate Total_Sales and round to 2 decimals
print("Calculating Total_Sales...")
data["Total_Sales"] = data["Quantity"] * data["Unit_Price"]
data["Total_Sales"] = data["Total_Sales"].round(2)

# Standardize text columns and formatting
print("Standardizing text columns and formatting...")
data["Category"] = data["Category"].str.title()
data["Payment_Method"] = data["Payment_Method"].str.replace(' ', '')
data["Store_Location"] = data["Store_Location"].str.title()
data["Product"] = data["Product"].str.title().str.replace(' ', '_')
data["Unit_Price"] = data["Unit_Price"].round(2)

print("\nSample of 10 rows after cleaning:")
print(data.sample(10))

# Sort by Date and reset index
print("Sorting data by 'Date' and resetting index...")
data.sort_values(by="Date", inplace=True)
data.reset_index(drop=True, inplace=True)

# Export cleaned data
print("Exporting cleaned data to CSV and Excel files...")
data.to_csv("../data/cleaned/supermarket_sales_cleaned.csv", index=False)
data.to_excel("../data/cleaned/supermarket_sales_cleaned.xlsx", index=False, sheet_name='Cleaned Data')

print("Data cleaning complete. Files saved to '../data/cleaned/'.")


