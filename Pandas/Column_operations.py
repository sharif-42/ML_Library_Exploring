import pandas as pd

d = {"A":[15, 20], "B":[20, 25], "C":[30 ,40], "D":[50, 60]}
df = pd.DataFrame(d)
print(df)

#insert a new column at last
c2 = df['C']*2
df['C2'] = c2
print(df)

# Similar Work
df = df.assign(c2 = df['C']*2)
print(df)

# Insert a new column at specific index/location
df.insert(3, "C3", df["C"]*3)
print(df)

