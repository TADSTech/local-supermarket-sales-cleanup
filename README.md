# Supermarket Sales Data Cleanup

This project cleans and standardizes a messy supermarket sales dataset using Python and pandas.

## Overview

The script `scripts/cleanup.py` performs the following steps:

1. **Loads the raw data** from an Excel file.
2. **Explores the data** with descriptive statistics, info, and random samples.
3. **Standardizes store location values** (e.g., merges all physical locations).
4. **Handles missing data** by:
   - Dropping rows with missing `Customer_ID` (likely walk-ins).
   - Dropping any remaining rows with missing values.
5. **Converts the `Date` column** to proper datetime format.
6. **Removes duplicate rows**.
7. **Calculates and rounds `Total_Sales`** for each transaction.
8. **Standardizes text columns** (e.g., title case, removes spaces, replaces spaces with underscores).
9. **Sorts the data by date** and resets the index for consistency.
10. **Exports the cleaned data** to both CSV and Excel formats in the `data/cleaned/` directory.

## Usage

1. Place the raw Excel file at `data/raw/messy_supermarket_sales.xlsx`.
2. Run the cleanup script:

   ```sh
   python scripts/cleanup.py
   ```

3. Find the cleaned data in:
   - `data/cleaned/supermarket_sales_cleaned.csv`
   - `data/cleaned/supermarket_sales_cleaned.xlsx`

## Requirements

- Python 3.x
- pandas
- numpy
- openpyxl (for Excel export)

Install dependencies with:

```sh
pip install requirements.txt
```

## Notes

- The script prints detailed progress and sample outputs at each step.
- All non-online store locations are unified as "Physical".
- All text columns are standardized for consistency.
- The cleaned data is sorted by date and indexed sequentially.

---
**Author:** TADSTech
**Last updated:** September 2025