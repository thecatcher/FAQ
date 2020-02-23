# def gen():
#     x = yield 1
#     print('gen---{0}'.format(x))
#     y = yield 2
#     print('gen---{0}'.format(y))
#     z = yield 3
#     print('gen---{0}'.format(z))
#
# g = gen()
#
# result0 = g.send(None)
# print('main---{0}'.format(result0))
# result1 = g.send(111)
# print('main---{0}'.format(result1))
# result2 = g.send(222)
# print('main---{0}'.format(result2))
# result3 = g.send(333)
# print('main---{0}'.format(result3))

##############################################################################

# def gen():
#     n=0
#     while True:
#         try:
#             yield n
#             n +=1
#         except OverflowError:
#             print("got it!")
#
# g = gen()
#
# result1 = next(g)
# print(result1)
#
# result2 = g.throw(OverflowError)
# print(result2)
#
# result3 = next(g)
# print(result3)


#########################################################################################
# import sys
# # def gen():
# #     n = 0
# #     while True:
# #         yield  n
# #         n+=1
# #
# # g = gen()
# #
# # result1 = next(g)
# # print(result1)
# #
# # try:
# #     result2 = g.throw(NameError)
# # except NameError:
# #     print('Main function catch the exception')
# #     print(sys.exc_info())
# #
# # try:
# #     print(result2)
# # except NameError:
# #     print('cathe NameError')
# #     print(sys.exc_info())
# #
# # print(next(g))


#########################################################################################

# import sys
#
# def gen():
#     try:
#         # 注意是在当前暂停的 yield 处抛出异常
#         # 所以要在这里捕获
#         yield 1
#     except Exception as e:
#         print('在生成器内部捕获了异常')
#         print(e.args)
#         print('处理完毕，假装什么也没发生')
#
#  #   yield 2
#
# g = gen()
#
# print(next(g))
#
# result = g.throw(TypeError,'类型错误~~')
#
# print(result)


#########################################################################################

def gen():
    try:
        yield 1
    except GeneratorExit:
        print('捕获到 GeneratorExit')
        print('尝试在 GeneratorExit 产生后 yield 一个值')
        yield 2

    print('生成器结束')


g = gen()
next(g)
g.close()


