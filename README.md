# Data Cleaning Automation Scripts
A project to clean messy CSV datasets using Python and Pandas. Includes reusable scripts and notebooks.

---

## 🗂 Project Overview
This repo contains reusable scripts that:
- Remove duplicates
- Fill missing values (mean, median, mode)
- Convert column types
- Save cleaned dataset

---

## 🛠 Tools & Tech
- Python (Pandas, NumPy)  
- Optional: SQL for database cleanup

---

## How to use
1. Clone the repository:
git clone https://github.com/yourusername/data-cleaning-python.git

2. Install dependencies: pip install -r requirements.txt

3. Place your raw CSV files in `data/raw/`.
  
4. Run the notebook or scripts to clean data and save outputs to `data/clean/`.

---

## Steps in the script

1. Load Dataset
Reads the raw CSV from the Data/Raw/ folder.

2. Remove Duplicates
Ensures all transactions are unique.

3. Fill Missing Values

- Numeric columns (Price Per Unit, Quantity, Total Spent) are filled with the column mean, rounded to 1 decimal.

- Text columns (Item, Category, Payment Method, Location) are filled with "Unknown".

- Discount Applied is filled with False and converted to boolean.

4. Convert Column Types
Converts Transaction Date to datetime for proper date handling.

5. Recalculate Total Spent
Corrects any inconsistencies: Total Spent = Price Per Unit × Quantity (rounded to 1 decimal).

6. Save Cleaned Dataset
Saves the cleaned CSV to the Data/Clean/ folder.

7. Preview Cleaned Data
Prints the first 10 rows of the cleaned dataset.

8. Optional Summary
Displays summary statistics for both numeric and categorical columns.

---

## Sample Data Source
https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning
