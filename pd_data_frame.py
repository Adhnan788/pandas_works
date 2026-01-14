"""

"""

import pandas as pd

students={
    "name":["adhnan","adhil","resin","shafi","libin"],
    "age":[21,22,23,20,25],
    "course":["ds","ds","st","dj","ds"]
}

df=pd.DataFrame(students)
print(df)

print(df[1:2])

print(df["course"])
print(df[["name","course","age"]])