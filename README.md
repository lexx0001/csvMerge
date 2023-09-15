# csvMerge

Documentation for Data Processing Script
========================================

This script is designed to read multiple CSV files from a specified folder, perform
calculations on specific columns, and then merge the resulting data frames into a single
CSV file.

Dependencies:
-------------
- pandas
- glob

Usage:
------
1. Place the CSV files you wish to process in the folder specified in the `csv_files` variable.
2. Run the script.

Modules:
--------
- pandas (as pd)
- glob

Variables:
----------
- csv_files: List of paths to CSV files that need to be processed.
- data_frames: List to store individual processed data frames before merging.

Functions and Loops:
--------------------
1. Loop through each CSV file defined in `csv_files`.
    - Read the CSV file into a DataFrame `df`.
    - Perform subtraction between columns with indices 2 and 3 to create a new column 'diff'.
    - Keep only the 'diff' column and the column with index 5.
    - Append this new DataFrame to `data_frames`.

2. Merge all the individual data frames stored in `data_frames` into `merged_df`.
3. Write `merged_df` into a new CSV file without index and header.
