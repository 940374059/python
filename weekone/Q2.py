import random
list=[]
zheng=[]
fu=[]
for i in range(50):
    list.append(random.randint(-10,10))
for j in list:
    if(j>0):
        zheng.append(j)
        continue
    elif j<0:
        fu.append(j)
        continue
print(list)
print(zheng)
print(fu)