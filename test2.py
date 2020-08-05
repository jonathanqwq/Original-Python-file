from random import *
import time
import os
print("正在出题中......")
print ()
time.sleep(2)
num = randint(1,2)
print("出题完成")
print ()
time.sleep(2)
if num == 1:
    print("请问什么老鼠两条腿走路？")
    print("1.米老鼠  2.小白鼠 3.普通老鼠")
    print ()
    time.sleep(1)
    ans_1=input("请输入你的回答：")
    print
    if ans_1 == "1":
        print("你真棒")
        os.system("pause")
    else:
        print("错了哦")
        os.system("pause")
if num == 2:
    print ("至少要多少时间才能读完清华大学？")
    print("1.4年  2.2秒 3.不知道")
    time.sleep(1)
    ans_2=input("请输入你的回答：")
    if ans_2 == "2":
        print("你真棒")
        os.system("pause")
    else:
        print("错了哦")
        os.system("pause")

