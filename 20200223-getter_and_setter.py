class Student(object):
    _school = 'xiaoerbi'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def school(self):
        return self._school

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if not s == 0:
            self._score = s


wangxiaoer = Student('wangxiaoer', 18)

print(wangxiaoer.age)
print(wangxiaoer.name)

wangxiaoer.score = 20

print(wangxiaoer.score)
print(wangxiaoer.school)
