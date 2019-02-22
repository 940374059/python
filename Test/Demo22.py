list=[]
count=0
for i in range(100,201):
    b=1
    for j in range(2,i):
        if(i%j==0):
            b=0
            break
    if(b==1):
        list.append(i)
        count+=1
print("质数",list)
print("数量:",count)
