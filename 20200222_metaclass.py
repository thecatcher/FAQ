# def choose_class(name):
#     if name == 'foo':
#         class Foo:
#             pass
#
#         return Foo
#     else:
#         class Bar:
#             pass
#
#         return Bar
#
#
# Myclass = choose_class('foo')
#
# print(Myclass)
# print(Myclass())

#############################################################################

# Foo = type('Foo', (object,), {'bar': True})
#
# print(Foo)
#
# foo = Foo()
#
# print(foo)
# print(foo.bar)


# def check_bar(self):
#     print(self.bar)
#
# Foochild = type('Foochild', (Foo,), {'check_bar':check_bar})
#
# myfoo=Foochild()
#
# print(myfoo)
# print(myfoo.check_bar())

#############################################################################

# Foo = type('Foo', (object,), {'bar': True})
#
#
# def get_bar(self):
#     print(self.bar)
#
#
# FooChild = type('FooChild', (Foo,), {'get_bar': get_bar})
#
# myfoo = FooChild()
#
# print(hasattr(FooChild,'get_bar'))
# print(myfoo)
# myfoo.get_bar()


#############################################################################

# def upper_attr(future_class_name, future_class_parents, future_class_attr):
#     attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
#     uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#     return type(future_class_name, future_class_parents, uppercase_attr)
#
#
# class MyMetacalss(object, metaclass=upper_attr):
#     bar = 'bip'
#
#
# print(hasattr(MyMetacalss, 'bar'))
# print(hasattr(MyMetacalss, 'BAR'))
#
# c = MyMetacalss()
# print(c.BAR)

#############################################################################

class Upper(type):
    def __new__(cls, name, bases, attrs):
        attr = ((name, value) for name, value in attrs.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attr)
        # return type.__new__(cls, name, bases, uppercase_attr)
        return super(Upper, cls).__new__(cls, name, bases, uppercase_attr)


class Myclass(metaclass=Upper):
    bar = 'bip'


c = Myclass()
print(c.BAR)
