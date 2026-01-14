import pandas as pd
salary=[30000,34000,35000,36000]

#series=pd.Series(salary)

#print(series[0])
#print(series[1])
#print(series[1:3])


series=pd.Series(salary,index=["e1","e2","e3","e4"])
print(series["e3"])
print(series["e1":"e4"])