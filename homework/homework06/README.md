# Homework 06 — Data Preprocessing

## Cleaning Strategy

The raw dataset was cleaned using reusable functions defined in `src/cleaning.py`.

### Missing Values

Missing values in the numeric columns `age`, `income`, and `score` were filled using the median of each respective column.

### Dropping Missing Data

Columns with more than 50% missing values were removed. The `extra_data` column was dropped because it contained a high proportion of missing values.

### Normalization

The `age`, `income`, and `score` columns were normalized using min-max scaling.

### Comparison

The original dataset had a shape of `(7, 6)` and contained missing values.

After cleaning, the dataset had a shape of `(7, 5)` with no missing values. The `extra_data` column was removed during preprocessing.

### Assumptions and Tradeoffs

Median imputation was chosen because it is less affected by extreme values than mean imputation.

A threshold of 50% missing values was used to determine when a column should be removed.

Min-max normalization was used to scale the selected numeric columns to a comparable range.

The cleaned dataset was saved to:

`data/processed/sample_data_cleaned.csv`