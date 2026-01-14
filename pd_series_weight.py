import pandas as pd

data=[60,70,64,69,68,70,62,53,75,77]

series=pd.Series(data)
print(series)

# head() list first 5 records
# tail() list last 5 records

print(series.head())
print(series.tail())

print(series.shape)