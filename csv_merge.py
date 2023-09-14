import pandas as pd
import glob

# Укажите индексы столбцов, которые вы хотите сохранить
# cols_to_keep = [2, 3, 5]  # В этом случае мы сохраняем 3, 4 и 6 столбцы

csv_files = glob.glob("C:/Users/lexx-/Desktop/dataARB/*.csv")

data_frames = []

for csv in csv_files:
    df = pd.read_csv(csv, header=None)
    # Делаем вычитание между столбцами с индексами 2 и 3 (третий и четвертый столбцы)
    df["diff"] = df.iloc[:, 2] - df.iloc[:, 3]
    # Сохраняем столбец с индексом 5 и новый столбец 'diff'
    df = df[["diff", 5]]
    data_frames.append(df)

merged_df = pd.concat(data_frames, ignore_index=True)

merged_df.to_csv("merged.csv", index=False, header=False)
