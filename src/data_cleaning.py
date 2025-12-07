# This script loads a messy sales dataset, cleans it, and saves a cleaned version.
# Each step is commented so the cleaning process is easy to understand.

import pandas as pd

# Function to load a CSV file into a DataFrame
def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df

# Function to clean column names (remove quotes, extra spaces, multiple underscores, lowercase)
def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()                  # Remove leading/trailing spaces
        .str.replace('"', '')         # Remove quotes
        .str.replace(' ', '_')        # Replace spaces with underscores
        .str.replace(r'_+', '_', regex=True)  # Replace multiple underscores with one
        .str.lower()                  # Lowercase everything
    )
    return df

# Function to handle missing numeric values
def handle_missing_values(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce').fillna(0)
    df['date_sold'] = pd.to_datetime(df['date_sold'], errors='coerce')  # Invalid/missing dates become NaT
    return df

# Function to remove invalid rows (negative price/qty)
def remove_invalid_rows(df):
    df = df[(df['price'] >= 0) & (df['qty'] >= 0)]
    return df

# Main script
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Load the raw CSV
    df_raw = load_data(raw_path)

    # Clean column names
    df_clean = clean_column_names(df_raw)
    print("Columns after cleaning:", df_clean.columns)

    # Handle missing values
    df_clean = handle_missing_values(df_clean)

    # Remove invalid rows
    df_clean = remove_invalid_rows(df_clean)

    # Save the cleaned data
    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())