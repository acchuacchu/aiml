import pandas as pd
import numpy as np
p=np.array([1,2,4,5])
print(" \n array create= \n",p)
info=pd.Series([10,35,65])
print(" \n series= \n ",info)
q=pd.Series(info)
print(" \n seies geving info= \n",q)
i=pd.Index([2,1,1,3,np.nan,3])
print("\n index= \n" ,i.value_counts())
a=pd.Series(4,[2,3,5,6])
print(a)
b=pd.Index([10,20,30,56,10,10,10,10,20])
print(b.value_counts())



