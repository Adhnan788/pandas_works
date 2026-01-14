import pandas as pd 
student_total={"s1":450,"s2":475,"s3":470,"s4":480,}

series=pd.Series(student_total)

print(series["s3"])