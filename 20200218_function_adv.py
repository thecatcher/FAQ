# def power_demo(x):
#     return x*x
#
# def foo(num1,num2,fun):
#     return fun(num1) + fun(num2)
#
# print(foo(2,3,power_demo))


# map()函数

# def f(x):
#     return x*x
# L = map(f,[1,2,3,4,5,6])
# print(type(L))
# print(list(L))
#
# for item in L:
#     print(item)

# reduce()函数
# from functools import reduce
#
# def foo(x,y):
#     return x*10+y
# result = reduce(foo,[1,3,5,7,9])
#
# print(type(result),result)

# filter()函数
# 定义一个生成器,输出所有奇数
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)


# g = primes()
#
# for i in range(1, 20):
#     print(next(g))
#     i += 1

def is_odd(x):
    return x % 2 == 1


# print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

# 闭包

# def print_msg():
#     msg = "hello world"
#
#     def printer():
#         print(msg)
#
#     # 注意,这里没带括号,返回的是printer()这个函数的引用(指针)
#     return printer
#
#
# # 这里等于通过print_msg()拿到了内部函数printer()的引用,所以printer这个变量指向了一个叫printer的函数
# printer = print_msg()
# print(printer)
# printer()

# def foo(x):
#     def foo_inner(y):
#         return x+y
#     return foo_inner
#
# foo1 = foo(5)
#
# print(foo1.__closure__)
# print(foo1.__closure__[0].cell_contents)

# lambda 表达式

# L = list(map(lambda x:x*x,[1,2,3,4,5]))
# print(L)
import functools


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         #这里是我们想增强的代码
#         print('this is a log: function "%s" is called'%func.__name__)
#         return func(*args, **kw)
#     return wrapper
def log(text):
    def decoraotor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s" % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decoraotor


@log("Holy shit!")
def now():
    print("2020-02-18")

# now()

def int2(x,base=2):
    return int(x,base)
print(int2('10000000'))

int22 = functools.partial(int,base=2)
print(int22('10000000'))