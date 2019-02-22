a=int(input("请输入数字"))
def dg(a):
    if(a==1):
        return  1
    else:
        return a*dg(a-1)
print(dg(a))