import pandas as pd
import numpy as np

d = {
    "col1": [2019, 2019, 2020],
    "col2": [350, 365, 1],
    "col3": [np.nan, 365, None]
}
data_frame = pd.DataFrame(d)

# Solution 1: Return the Total missing values in all data frame
print("Total Missing Values in whole Dataset ")
print(data_frame.isnull().sum().sum())

# Solution 2: Return the column wise count
print("Missing Values in all Dataset In each Column")
print(data_frame.isna().sum())

# # Solution 3: Return the boolean representation for each column
print("Total Missing Values in all Dataset In each Column")
print(data_frame.isna().any())

# Solution 4: Return True for at least one missing value otherwise False
print("Return True for at least one missing value otherwise False ")
print(data_frame.isna().any(axis=None))
