import pandas as pd
import os

csv_file = "caxton_dataset_filtered_og.csv"
df = pd.read_csv(csv_file)

# base_dir = ""
# df = df[df['img_path'].apply(lambda path: os.path.exists(os.path.join(base_dir, path)))]

df = df[df['img_path'].apply(lambda path: os.path.exists(path))]

df.to_csv("caxton_dataset_filtered.csv", index=False)
