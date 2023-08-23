import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/titanic.csv")
print(data)
print(pd.DataFrame(data))
c=data.dropna()
print(c.sum())
print(c['Survived'].sum())
print(c.value_counts())
print(c['PassengerId'].value_counts())
print(c.agg(['sum','max','min']))


