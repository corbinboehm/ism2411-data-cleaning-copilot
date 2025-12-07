# This script loads a messy sales dataset, cleans it, and saves a cleaned version.
# Each cleaning step is explained in the comments so the process is clear.

import pandas as pd

# Copilot function 1: load the raw data
# This function should read a CSV file and return it as a DataFrame.
def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df

# Copilot function 2: clean and standardize column names
# This function should lowercase all column names and replace spaces with underscores.
def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

# Handle missing values (you will tweak this later)
def handle_missing_values(df):
    # Remove rows where price or quantity is missing because those rows can’t be used
    df = df.dropna(subset=["price", "quantity"])
    return df

# Remove invalid rows
def remove_invalid_rows(df):
    # Rows with negative price or quantity are clearly errors
    df = df[(df["price"] >= 0) & (df["quantity"] >= 0)]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())