x=lambda a:a+10
print(x(5))

lst=[2,5,4]
a=list(map(lambda x:x+5,lst))
print(a)

lst=[1,2,3]
sqrt=list(map(lambda y:y*y,lst))
print(sqrt)

fib=[34]
f=list(filter(lambda x:x%2==0,fib))
print(f)

from functools import reduce
lst=[1,2,3,4,5,6,7]
x=reduce(lambda x,y:x+y,lst)
print(x)

lst=[1,2,3,4,5,6,7]
x=reduce(lambda x,y:x<y,lst)
print(x)

lst1=[1,2,3,6]
lst2=[5,8,3,2]
lst3=[9,3,6,7]
q=list(map(lambda x,y,z:x+y+z,lst1,lst2,lst3))
print(q)

fruits=['mango','orange','apple','kiwi']
a=list(filter(lambda x:'g' in x,fruits))

print(a)



