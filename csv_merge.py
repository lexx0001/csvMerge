import pandas as pd
import glob

# Specify the indices of the columns you want to keep
# cols_to_keep = [2, 3, 5]  # In this case, we keep columns 3, 4, and 6

csv_files = glob.glob("C:/Users/lexx-/Desktop/dataARB/*.csv")

data_frames = []

for csv in csv_files:
    df = pd.read_csv(csv, header=None)
    # Perform subtraction between columns with indices 2 and 3 (third and fourth columns)
    df["diff"] = df.iloc[:, 2] - df.iloc[:, 3]
    # Keep the column with index 5 and the new 'diff' column
    df = df[["diff", 5]]
    data_frames.append(df)

merged_df = pd.concat(data_frames, ignore_index=True)

merged_df.to_csv("merged.csv", index=False, header=False)
