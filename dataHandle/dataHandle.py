import pandas as pd
import numpy as np

# 1. Load
df = pd.read_csv("data.csv")

# 2. Inspect
print(df.head())
print(df.info())
print("space--------")
# 3. Handle missing values
print(df.isna().sum())                           # count missing per column
df["age"] = df["age"].fillna(df["age"].median()) # fill numeric gaps
df = df.dropna(subset=["name"])                  # drop rows missing a key field

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Filter
adults = df[df["age"] >= 18]

# 6. Basic stats
print(df.describe())
print("Mean age:", np.mean(df["age"]))
print(df.groupby("city")["salary"].mean())

# 7. Convert to NumPy array
X = df[["age", "salary"]].to_numpy()
print(X.shape)