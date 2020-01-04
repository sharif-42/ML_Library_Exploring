import pandas as pd

d = {
    "year": [2016, 2019, 2019, 2020],
    "day_of_year": [366, 350, 365, 1]
}

df = pd.DataFrame(d)
print(df)

# Step 1: create a combined column
df["combined"] = df["year"] * 1000 + df["day_of_year"]
print(df)

# Step 2: convert to datetime
df["date"] = pd.to_datetime(df["combined"], format="%Y%j")
print(df)
