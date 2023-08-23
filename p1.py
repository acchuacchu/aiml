import pandas as pd
data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/titanic.csv")
print(data)
print(data.info())
print(data.shape)
print(data.loc[data['Age']>50])
print(data.iloc[5:10,2:4])
