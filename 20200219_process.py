# import os
# from multiprocessing import Process
#
# # 一个没看懂的多进程的例子
# def run_proc(name):
#     print('Run child process %s(%s)'%(name,os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' %os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print("Child process will start.")
#     p.run()
#     p.start()
#     p.join()
#     print('Child process end.')

###############################################################

# from multiprocessing import Process
# import  time
#
# def worker(interval):
#     n=5
#     print('worker start!')
#     while n>0:
#         print('The time is {0}'.format(time.ctime()))
#         time.sleep(interval)
#         n -=1
#
# if __name__ == '__main__':
#     p = Process(target=worker,args=(3,))
#     p.start()
#     p.join(1)
#     time.sleep(2)
#     print(p.pid)
#     print(p.name)
#     print(p.is_alive())

###############################################################

# import multiprocessing
# import time
#
#
# def worker_1(interval):
#     print('worker_1')
#     time.sleep(interval)
#     print('end worker_1')
#
#
# def worker_2(interval):
#     print('worker_2')
#     time.sleep(interval)
#     print('end worker_2')
#
#
# def worker_3(interval):
#     print('worker_3')
#     time.sleep(interval)
#     print('end worker_3')
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=worker_1,args=(2,))
#     p2 = multiprocessing.Process(target=worker_2, args=(3,))
#     p3 = multiprocessing.Process(target=worker_3, args=(4,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print('The number of CPU is:'+str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('Child  p.name:'+p.name+' p.id:'+str(p.pid))
#     print('END')

###############################################################

# import multiprocessing
# import time
#
# class MyProcess(multiprocessing.Process):
#     def __init__(self,interval):
#         multiprocessing.Process.__init__(self)
#         self.interval = interval
#
#     def run(self):
#         for i in range(1,5):
#             print('the time is {0}'.format(time.ctime()))
#             time.sleep(self.interval)
#
# if __name__ == '__main__':
#     p = MyProcess(5)
#     p.start()

###############################################################

# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print("Run task %s(%s)..." % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s run %.2f second' % (name, (end - start)))
#
# if __name__ == '__main__':
#     print('Parent process %s',os.getpid())
#     pool= Pool(4)
#     for i in range(5):
#         pool.apply_async(long_time_task,args=(i,))
#     print('waiting for all subprocess done...')
#     pool.close()
#     pool.join()
#     print('All subprocess done!')

###############################################################

import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
