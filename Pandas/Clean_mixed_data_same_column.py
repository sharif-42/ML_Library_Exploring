import pandas as pd

d = {
    "customer": ["A", "B", "C", "D"],
    "sales": [1100, 950.75, "$400", "$1250.35"]
}
df = pd.DataFrame(d)

# Step 1: check the data types
print(df["sales"].apply(type))

# Step 2: use regex
df["sales"] = df["sales"].replace("[$,]", "", regex=True).astype("float")
print(df)

print(df["sales"].apply(type))
