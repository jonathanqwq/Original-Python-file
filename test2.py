from random import *
import time
import os
print("正在出题中......")
time.sleep(1)
# -*- coding: UTF-8 -*-

import sys, time

class ShowProcess():
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    i = 0 # 当前的处理进度
    max_steps = 0 # 总共需要处理的次数
    max_arrow = 50 #进度条的长度
    infoDone = 'done'

    # 初始化函数，需要知道总共的处理次数
    def __init__(self, max_steps, infoDone = 'Done'):
        self.max_steps = max_steps
        self.i = 0
        self.infoDone = infoDone

    # 显示函数，根据当前的处理进度i显示进度
    # 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps) #计算显示多少个'>'
        num_line = self.max_arrow - num_arrow #计算显示多少个'-'
        percent = self.i * 100.0 / self.max_steps #计算完成进度，格式为xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' #带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(process_bar) #这两句打印字符到终端
        sys.stdout.flush()
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0

if __name__=='__main__':
    max_steps = 100

    process_bar = ShowProcess(max_steps, '出题完成')

    for i in range(max_steps):
        process_bar.show_process()
        time.sleep(0.01)
print ()
time.sleep(2)
num = randint(1,2)
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

