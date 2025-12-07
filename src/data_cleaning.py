# This script loads a messy sales dataset, cleans it, and saves a cleaned version.
# Each step is commented so the cleaning process is easy to understand.

import pandas as pd

# Function to load a CSV file into a DataFrame using pandas
# This reads the raw sales data so we can clean it later.
def load_data(file_path: str):
    df = pd.read_csv(file_path)    # Copilot suggested a one-liner; I added a variable for clarity.
    return df

# Function to clean column names by lowercasing, replacing spaces with underscores,
# and stripping extra underscores from start/end
def clean_column_names(df):
    df.columns = df.columns.str.lower() \
                            .str.replace(' ', '_') \
                            .str.strip('_')  # Remove leading/trailing underscores
    return df

# Function to handle missing values in price and quantity columns
# We will fill missing values with 0 to keep calculations safe
def handle_missing_values(df):
    df['price'] = pd.to_numeric(df['price'].astype(str).str.strip(), errors='coerce').fillna(0)   # Fill missing or invalid prices with 0
    df['qty'] = pd.to_numeric(df['qty'].astype(str).str.strip(), errors='coerce').fillna(0)       # Fill missing or invalid quantities with 0
    return df

# Function to remove rows with invalid data
# Negative prices or quantities are considered data entry errors and should be removed
def remove_invalid_rows(df):
    df = df[(df['price'] >= 0) & (df['qty'] >= 0)]  # Keep only rows with non-negative price and quantity
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Load the raw CSV
    df_raw = load_data(raw_path)

    # Clean column names
    df_clean = clean_column_names(df_raw)
    print("Columns after cleaning:", df_clean.columns)

    # Handle missing values using updated column names
    df_clean = handle_missing_values(df_clean)

    # Remove invalid rows using updated column names
    df_clean = remove_invalid_rows(df_clean)

    # Save the cleaned data
    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())