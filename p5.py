import pandas as pd
data=pd.DataFrame({"Days":[1,2,3,4,5,6,7,8,9,10],
                   "steps":[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]})
print(data)
df=pd.DataFrame(data)
df['steps']= df['steps']+1000
print(df)
   
a=df[df['steps']>7000] ['Days']
print(list(a))

