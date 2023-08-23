import numpy as np
import pandas as pd
data=pd.read_csv("C:/Users/SPTINT-08/Desktop/iris/Iris.csv")
print("\n csv file \n",data)
df= data.head(5)
print(df)
data1=pd.Series(data['Species'])
print("\n series \n",data1.value_counts())
data2=pd.DataFrame(data1)
print("\n dtaframes=",data2)
data3=pd.DataFrame(data['SepalLengthCm'])
print(data3)
data4=pd.DataFrame(data['PetalLengthCm'])
print(data4)
data5=pd.concat([data3,data4],axis=1)
print(data5)



a=pd.DataFrame(df['PetalWidthCm'])
print(a)
b=pd.DataFrame(df['SepalWidthCm'])
print(b)
c=pd.concat([a,b],axis=1)
print(c)

