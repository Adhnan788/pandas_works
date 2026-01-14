import pandas as pd

employee={"e1":15000,"e2":20000,"e3":30000,"e4":40000}

series=pd.Series(employee)
print(series)

print("total",series.sum())
print("max",series.max())
print("min",series.min())
print("average",series.mean())
