phone=input("请输入您手机号:")
list=[138,136,182,176,135]
try:
    int(phone)
    if(len(phone)==11):
        str=phone[0:3]
        bool=False
        for i in list:
            if(int(str)==i):
               bool=True
               break
        if(bool):
            print("有效手机号!")
        else:
            print("无效手机号！")


    else:
        print("您输入的手机号不符合")
except ValueError:
    print("手机号输入不符合")