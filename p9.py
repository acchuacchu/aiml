import pandas as pd
import numpy as np
data=pd.DataFrame({"first score":[10,20,np.nan,30],
                   "second score":[np.nan,10,21,43],
                   "third score":[10,20,30,np.nan]})
print(data)
print(data.isnull())
print(data.notnull())
print(data.fillna(5))
print(data.fillna(method="pad"))

print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-100))
print(data.dropna())
print(data.dropna(how="all"))





