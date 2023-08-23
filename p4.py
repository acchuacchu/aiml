#lambda function
a=lambda x : x+5
print("adding 5 to add",a(3))

b=lambda x,y : x+y
print("adding 2 numbers ",b(3,5))

c=lambda x,y : x if(x>y)else y
print("greatest number",c(4,9))

d=lambda x:x*x
print("multiplication in squarr",d(5))

e=lambda a :a**2
print("multiplication in squarr",e(6))

#map function
lst=[1,2,3,4,5,6,8,8]
l1=list(map(lambda x : x+5,lst))
print("mapping",l1)

#filter function
l2=[1,4,6,8,5,9,4,9]
l3=list(filter(lambda x:x%2,l2))
print("filter odd numbers",l3)
l8=list(filter(lambda x:x%2==0,l2))
print("filter even numbers",l8)

#reduce function
from functools import reduce 
l4=[65,8,9,34,7,95,854,9]
l5=reduce(lambda x,y:x+y,l4)
print("reduce ",l5)










