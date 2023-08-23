import numpy as np
import pandas as pd
ser1=pd.Series([1,32,4,6,7,8])
ser2=pd.Series([1,4,8,45,67,5])
u=pd.Series(np.union1d(ser1,ser2))
print("\n union = \n ",u)
i=pd.Series([np.intersect1d(ser1,ser2)])
print(" \n intersect= \n",i)
nc=u[~u.isin(i)]
print(" \n not  common in two series= \n",nc)


