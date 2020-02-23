# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 ok'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#  c   n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return %s' % r)
#     c.close()
#
#
# c = consumer()
# produce(c)

################################################################

# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print('hello world')
#     r = yield from asyncio.sleep(2)
#     print('hello world again!')
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()
################################################################
# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('hello world!  (%s)' % threading.current_thread())
#     yield from asyncio.sleep(2)
#     print('hello world again (%s)' % threading.current_thread())
#
#
# loop = asyncio.get_event_loop()
# task = [hello(), hello()]
# # loop.run_until_complete(asyncio.wait(task))
# # loop.close()
#
# aws,futures = asyncio.wait(task)
# print(aws)
# print(futures)
################################################################

# import asyncio
# import time
#
# async def so_some_work(x):
#     print('waiting: ',x)
#
# now = lambda :time.time()
#
# start = now()
#
# coroutine = so_some_work(2)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
#
# print('TIME: ',now() - start)


################################################################

# import asyncio
# import time
#
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#
#
# now = lambda: time.time()
#
# start = now()
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print(task)
#
# loop.run_until_complete(task)
# print(task)
# print('TINE: ', now() - start)

################################################################

# import asyncio
# import time
# import functools
#
#
# async def so_some_work(x):
#     print('Waitting: ', x)
#     return 'Done after {0}s'.format(x)
#
#
# def callback(future):
#     print('Callback: ', future.result())
#
#
# def callback2(t, future):
#     print('Callback: ', t, future.result())
#
#
# now = lambda: time.time()
#
# start = now()
#
# coroutine = so_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# # task.add_done_callback(callback)
# task.add_done_callback(functools.partial(callback2, 2))
# loop.run_until_complete(task)
#
# print('TIME: ', now() - start)

################################################################


# import asyncio
# import time
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waitting: ', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
#
# start = now()
#
# coroutine1 = do_some_work(1)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(4)
# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(coroutine1),
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3)
# ]
#
# loop.run_until_complete(asyncio.wait(tasks))
#
# for task in tasks:
#     print('Task ret: ', task.result())
# print('TIME: {}'.format(now() - start))

################################################################

# import asyncio
# import time
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waitting: ', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
#
# async def foo():
#     coroutine1 = do_some_work(1)
#     coroutine2 = do_some_work(2)
#     coroutine3 = do_some_work(4)
#
#     tasks = [
#         asyncio.ensure_future(coroutine1),
#         asyncio.ensure_future(coroutine2),
#         asyncio.ensure_future(coroutine3)
#     ]
#     dones, pendings = await  asyncio.wait(tasks)
#
#     for task in dones:
#         print('Task ret: ', task.result())
#
#
# start = now()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(foo())
#
# print('TIME: ', now() - start)

################################################################

import asyncio
import time

now = lambda :time.time()

async def do_some_work(x):
    print('Waitting: ',x)
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))

corutine1 = do_some_work(1)
corutine2 = do_some_work(2)
corutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(corutine1),
    asyncio.ensure_future(corutine2),
    asyncio.ensure_future(corutine3)
]

start = now()

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print('TIME: ', now()-start)