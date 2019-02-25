try:
    a=int(input("请输入手机号"))
except ValueError:
    print("数字类型错误")
else:
    print("其他错误")
finally:
    print("一定要好好学习")