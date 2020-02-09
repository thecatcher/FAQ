# 最简单的生成器
def generator_simple_demo():
    # 最简单的生成器
    L = [x * x for x in range(10)]
    print(type(L))
    # 这就是一个最简单的生成器
    g = (x * x for x in range(10))
    print(type(g))
    # 使用的时候用for循环,会自动调用next()函数
    for eg in g:
        print(eg, end=' ')


# 斐波那契数列
# 常规函数法
def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


# 生成器大法
def fib_g(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        a, b = b, a + b
        n += 1
    return 'ahahahhaha~done'


# 注意使用yield的时候,条件不满足的时候,yield直接就退出方法了,所以下面的return是不生效的.
# 如果非要得到yield之后的返回值的话,就需要捕获StopIteration异常才可以return 'done'
def fib_g_test():
    g = fib_g(6)
    while True:
        try:
            print(next(g), end=' ')
        except StopIteration as e:
            print(e.value)
            break


fib_g_test()
