import os
age=input("请输入你的年龄：")
name=input("请输入你的名字：")
print("你的年龄是：")
print(age)
print("你的名字是：")
print(name)
os.system("pause")
print("请一定输入数字！否则系统将出现问题！")
num = input("请输入：1+1=")
if(num>0):
	if(num>2):
		print("大了哦")
	elif(num<2):
		print("小了哦")
	else:
		print("正确")
else:
	print("请输入正确数字！")
os.system("pause")
