
print(list(filter( lambda x: not x%2, range(0,100))))


'''
import threading
import time
# import win32api # 引用系统函数

class Mythead(threading.Thread):# 写一个类继承 threading.Thread 这个类，重写run函数
    def run(self): #run重写 实现 线程开启后运行函数
        print("Mythread")

for i in range(5):
    t=Mythead() # 初始化
    t.start() # 开启线程

while True:
    pass
'''
'''
#基于类实现多线程
import threading
import time
# import win32api # 引用系统函数

class Mythead(threading.Thread):# 写一个类继承 threading.Thread 这个类，重写run函数
    def run(self): #run重写 实现 线程运行函数
        print("Mythread")

for i in range(5):
    t=Mythead() # 初始化
    t.start() # 开启线程

while True:
    pass
'''
'''
# 线程冲突
import _thread
import time
num=0

def add():
    global num
    for i in range(100000):
        num+=1
    print(num)

for i in range(5):
    _thread.start_new_thread(add,())

while True:
    pass
'''
'''
import socket #网络通信TCP,UDP
import _thread
mystr="1_lbt4_10#32899#002481627512#0#0#0:1289671407:你的baby:你的hello:288:你好妹子" #这个字符串，通过飞Q通信分析才能得到

count=0

def go(i):
    udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # udp
    udp.connect(("10.10.153."+str(255-i),2425))
    udp.send(mystr.encode("gbk"))
    print(i)

for i in range(255):
    _thread.start_new_thread(go,(i,))
    count=i
    print("i=",i)

while True:
    if count == 254:
        break
'''

'''
import _thread
import time

def go():
    for i in range(10):# 10 秒
        print(i,"------")
        time.sleep(1)

for i in range(5): # 50秒
    _thread.start_new_thread(go,())# 5个线程 跑一个10秒的函数

for i in range(12):
    time.sleep(1)

print("game over")
'''
'''
import win32api # 引用系统函数
import _thread  # 多线程
def show():
    win32api.MessageBox(0,"你的账户很危险","来自支付宝的问候",6)
#顺序执行
#for i in range(5):
    #show()
for i in range(5):
    _thread.star_new_thread(show,()) # ()元组
'''
































