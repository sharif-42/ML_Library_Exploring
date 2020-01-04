import pandas as pd

# Load Data
data_frame = pd.read_csv('dataset/person.csv')
print(data_frame.head(4))

data_frame.plot(kind="scatter", x="id", y="age").show()


