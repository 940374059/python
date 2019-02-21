import random
list=[]
for i in range(20):
    list.append(random.randint(0,10))
print(list)
print("列表长度是:",len(list))
list[::2]=sorted(list[::2],reverse=True)
print("排序后",list)
