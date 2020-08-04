import os
age=input("请输入你的年龄：")

name=input("请输入你的名字：")

print("你的年龄是：")
print(age)
print("你的名字是：")
print(name)


ans=input("确认请输入Y，有错误请输入N:")

if ans=="Y":
    print("请一定输入数字！否则系统将出现问题！")
    num = int(input("请输入：1+1="))
    if num>0:
        if(num>2):
            print("大了哦")
        elif(num<2):
            print("小了哦")
        else:
            print("正确")
    else:
        print("请输入正整数！")
os.system("pause")
if ans=="N":

    age=input("请输入你的年龄：")


    name=input("请输入你的名字：")

    print("你的年龄是：")
    print(age)
    print("你的名字是：")
    print(name)



    ans=input("确认请输入Y，有错误请重新运行代码")
    
    if ans=="Y":
        print("请一定输入数字！否则系统将出现问题！")
        num = int(input("请输入：1+1="))
        if num>0:
            if(num>2):
                print("大了哦")
            elif(num<2):
                print("小了哦")
            else:
                print("正确")
        else:
            print("请输入正整数！")
os.system("pause")
