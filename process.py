import functools
loop=3
print(functools.reduce(lambda x,y:x+y, range(1,loop+1)))

#print(float('inf'))

'''
# a,b=(1,2)
# print(a,b) a=1,b=2

import multiprocessing
import os
def func(conn): #conn 管道类型 双向通信
    conn.send(["a","b","c","d","e"])#发送的数据
    print(os.getpid(),conn.recv())#收到的数据
    conn.close()#关闭

if __name__=="__main__":
    conn_a,conn_b=multiprocessing.Pipe()#创建一个管道，两个口
    #print(id(conn_a),id(conn_b))
    #print(type(conn_a),type(conn_b))#multiprocessing.connection.PipeConnection
    p=multiprocessing.Process(target=func,args=(conn_a,))
    p.start()
    conn_b.send([1,2,3,4,5,6,7])
    print(os.getpid(),conn_b.recv())
    p.join()
'''
'''
#a,b=(1,2)
#print(a,b) a=1,b=2

import multiprocessing
import os
def func(conn):#conn管道类型 双向通信
    conn.send(["a","b","c","d","e"])#发送的数据
    print(os.getpid(),conn.recv())#收到的数据
    conn.close()#关闭

if  __name__=="__main__":
    conn_a,conn_b=multiprocessing.Pipe()#创建一个管道，两个口
    #print(id(conn_a),id(conn_b))
    #print(type(conn_a), type(conn_b)) #multiprocessing.connection.PipeConnection
    p=multiprocessing.Process(target=func,args=(conn_a,))
    p.start()
    conn_b.send([1,2,3,4,5,6,7])
    print(os.getpid(),conn_b.recv())
    p.join()
'''
'''
import  os
import multiprocessing
import time
#多进程，并发，乱序并发执行
#多进程加锁，挨个执行，仍然是乱序

def  showdata(lock,i):
    with lock:
        time.sleep(2)
        print(i)

if __name__=="__main__":
    lock=multiprocessing.RLock()#创建锁
    for num in range(10):
        multiprocessing.Process(target=showdata,args=( lock,num)).start()
'''
'''
import  os
import multiprocessing
import time

def info(title):
    print(title)
    time.sleep(2)
    print(__name__)
    print("father ppid",os.getppid())
    print("self pid", os.getpid())
    print("-----------")

if  __name__=="__main__":
    p1 =multiprocessing.Process(target=info,args=("A1",))
    p2 = multiprocessing.Process(target=info, args=("A2",))
    p3 = multiprocessing.Process(target=info, args=("A3",))
    p1.start() #并发干活
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    info("hello")
    print("all over") # 上面并发干完活了，这里就可以做汇总工作了
'''
'''
       #进程轮流干活
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
'''
'''
import os
import multiprocessing #多进程模块

def info(title):
    print(title)
    print(__name__)
    print("father ppid",os.getppid())
    print("self pid",os.getppid())
    print("----------")

if __name__ == "__main__":
    info("hello")

    #多进程
    p=multiprocessing.Process(target=info,args=("gaoqinghua",))
    p.start()
    p.join()#父进程必须等待子进程干完活，执行后续代码
    print("hello hechengcheng")
'''

'''
import os
print("hello china")

pid=os.fork()
print("hefengcheng is boy")
print("sunyu is boy")
print(pid)

if pid==0:
    print("pid==0","i am son")
else:
    print("pid!=0","i am father")

'''















