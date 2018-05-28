
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing

# 管道消费者.
def consumer(lock,pipe):
    output_p, input_p = pipe
    input_p.close() # 关闭管道输入口
    while True:
    lock.acquire()            
    item = output_p.recv()
    lock.release()
    if item == None:    
            break
        
        # 处理部分
        lock.acquire()
        print(item)
        lock.release()

# 管道生产者
def producer(sequence, input_p):
    for item in sequence:
        # Put the item on the queue
        input_p.send(item)
        
if __name__ == '__main__':
    
    # 进程数、创建管道，锁等
    p_num = 2
    process = []    
    (output_p, input_p) = multiprocessing.Pipe()
    lock = multiprocessing.Lock()
    
    # 定义消费进程
    for i in range(p_num):
        t =multiprocessing.Process(target=consumer,args=(lock,(output_p, input_p),))      
        t.daemon=True
        process.append(t)    

    # 启动消费进程
    for i in range(p_num):
        process[i].start()
        
    # 关闭输出管道，以往管道填充数据
    output_p.close()
    sequence = range(100) + [None]*p_num   
    producer(sequence, input_p)    
    # 数据填充完毕，打开输入管道
    input_p.close()
    
    # 等待结束
    for i in range(p_num):
        process[i].join()