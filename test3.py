

from turtle import *
import os

#请从bg1.png,bg2.png,bg3.png中选择一个地图

print("今天，我们要让小海龟吃到宝石。")
print("请一定看到最后！")
input("明白请输入Y：")
print("程序正式开始啦！")
print("备注：1、程序中的左右是以小乌龟面向的方向哦")
print("      2、程序中如果输入错误，系统将会自动退出")
Screen().bgpic("bg3.png")

t=Turtle()
t.shape("turtle")
#请你帮助小海龟前进、左转、右转吧~
t.right(90)
ans=input("请问，小乌龟现在应该往哪里走？（l=左转 r=右转 f=前进）")
if ans=="f":
    print("恭喜你，答对啦！")

    t.forward(50)
    ans1=input("请问，小乌龟现在应该往哪里走？（l=左 r=右 f=前）")
    if ans1=="r":
        print("恭喜你，答对啦！")
        
        t.right(90)
        t.forward(70)
        ans2=input("请问，小乌龟现在应该往哪里走？（l=左 r=右 f=前）")
        if ans2=="l":
            print("恭喜你，答对啦！")
            
            t.left(90)
            t.forward(70)
            ans3=input("请问，小乌龟现在应该往哪里走？（l=左 r=右 f=前）")
            if ans3=="r":
                print("恭喜你，答对啦！")
                
                t.right(90)
                t.forward(90)
                ans4=input("请问，小乌龟现在应该往哪里走？（l=左 r=右 f=前）")
                if ans4=="r":
                    print("恭喜你，答对啦！")
                    
                    t.right(90)
                    t.forward(110)
                    ans5=input("请问，小乌龟现在应该往哪里走？（l=左 r=右 f=前）")
                    if ans5=="l":
                        print("恭喜你，答对啦！")
                    
                        t.left(90)
                        t.forward(150)
                            
                        print("彩蛋时间到！")
                        t.right(180)
                        t.forward(150)
                        t.right(90)
                        t.forward(110)
                        t.left(90)
                        t.forward(90)
                        t.left(90)
                        t.forward(70)
                        t.right(90)
                        t.forward(70)
                        t.left(90)
                        t.forward(50)
                        t.left(90)
                        t.right(135)

                        for i in range(80):
                            t.forward(1)
                        for i in range(110):
                            t.left(2)
                            t.forward(1)
                        t.right(180)
                        for i in range(110):
                            t.left(2)
                            t.forward(1)
                        t.forward(80)

os.system("pause")