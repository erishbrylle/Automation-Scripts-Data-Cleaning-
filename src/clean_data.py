import pandas as pd
import numpy as np

# Suppress Pandas 3+ downcasting warnings
pd.set_option('future.no_silent_downcasting', True)

# -----------------------
# Load dataset
# -----------------------
def load_data(file_path):
    """Load CSV file into a DataFrame."""
    return pd.read_csv(file_path)

# -----------------------
# Remove duplicates
# -----------------------
def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates(ignore_index=True)

# -----------------------
# Fill missing values
# -----------------------
def fill_missing_values(df):
    """
    Fill missing values in the dataset.
    - Numeric columns: fill NaN with mean (1 decimal)
    - Text columns: fill NaN with 'Unknown'
    - Discount Applied: convert to bool, fill NaN with False
    """
    # Numeric columns
    for col in ['Price Per Unit', 'Quantity', 'Total Spent']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            mean_val = round(df[col].mean(), 1)
            df[col] = df[col].fillna(mean_val)
            df[col] = df[col].round(1)

    # Text columns
    for col in ['Item', 'Category', 'Payment Method', 'Location']:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')

    # Discount Applied column
    if 'Discount Applied' in df.columns:
        df['Discount Applied'] = df['Discount Applied'].astype('bool', errors='ignore')
        df['Discount Applied'] = df['Discount Applied'].fillna(False)

    return df

# -----------------------
# Convert column types
# -----------------------
def convert_column_types(df):
    """Convert Transaction Date to datetime."""
    if 'Transaction Date' in df.columns:
        df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
    return df

# -----------------------
# Recalculate Total Spent
# -----------------------
def recalc_total_spent(df):
    """Recalculate Total Spent = Price Per Unit * Quantity (1 decimal)."""
    if 'Price Per Unit' in df.columns and 'Quantity' in df.columns:
        df['Total Spent'] = (df['Price Per Unit'] * df['Quantity']).round(1)
    return df

# -----------------------
# Save cleaned dataset
# -----------------------
def save_clean_data(df, file_path):
    """Save DataFrame to CSV."""
    df.to_csv(file_path, index=False)
