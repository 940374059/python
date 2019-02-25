import re
a = input("请输入您的邮箱")
def Email(a):
    str = r'^[0-9a-zA-Z.]+@[0-9a-zA-Z.]+?com$'
    if re.match(str,a):
        print("邮箱符合！")
    else:
        print("不符合")
Email(a)