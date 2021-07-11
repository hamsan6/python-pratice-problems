# Problem: Find sum of numbers which have 3 distinct factors (from input or a list)

import sys

line1 = '1,3,6,7,21'

print(line1)

list1=line1.split(sep=',')

print(list1)


# function to find factors
def factors_fn(x):
    factor=[]
    for i in range (1,x+1):
        if x%i==0:
            factor.append(i)
    return factor       
         

# d2--> will be list of numbers with 3 distint factors
d2=[]

for n in range(len(list1)):
    p=factors_fn(int(list1[n]))
    print(list1[n], p, len(p))
    #print(len(p))
    if(len(p)>=3):
        d2.append(int(list1[n]))

print(sum(d2))        

# OR ----

# d2--> will be list of numbers with 3 distint factors
d2=[]

for n in (list1):
    p=factors_fn(int(n))
    print(p)
    if(len(p)>=3):
        d2.append(int(list1[n]))

print(sum(d2))
    
    