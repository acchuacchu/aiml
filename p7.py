import pandas as pd
data=pd.DataFrame([[1,2,3,45],[8,57,4,88],[6,8,9,3]],columns=["maths","science","kannada","english"])
print(data)
print(data.sum())
print(data['maths'].sum())
print(data.value_counts())
print(data['english'].value_counts())
print(data.agg(['sum','max','min']))
print(data.describe())


