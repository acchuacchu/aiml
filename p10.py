import pandas as pd
import numpy as np
data=data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/titanic.csv")
print(data)
print(pd.DataFrame(data))
print(data.isnull())
print(data.notnull())
print(data.fillna(5))
print(data.fillna(method="pad"))
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-100))
print(data.dropna())
print(data.dropna(how="all"))

