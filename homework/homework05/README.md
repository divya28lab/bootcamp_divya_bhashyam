# Homework 05 — Data Storage

## Data Storage

### Folder Structure

- data/raw/ stores raw data in CSV format.
- data/processed/ stores processed data in Parquet format.

Formats Used

- CSV is used for the raw dataset because it is simple, portable, and easy to inspect.
- Parquet is used for the processed dataset because it is a columnar format that preserves data types and is efficient for analytical workloads.

Environment-Driven Paths

The storage paths are configured through .env:
- DATA_DIR_RAW=data/raw
- DATA_DIR_PROCESSED=data/processed

The notebook loads these variables using python-dotenv and creates the directories if they do not already exist.

Validation:

- After saving, both CSV and Parquet files are reloaded.
The validation checks confirm:
- The reloaded shape matches the original DataFrame.
- The date column remains a datetime type.
- The price column remains numeric.

Assumptions:

- The sample dataset contains 20 daily AAPL observations with date, ticker, and price columns.
- Timestamped filenames are used so previous outputs are not overwritten.
- The .env file contains environment-specific configuration and is excluded from version control.
