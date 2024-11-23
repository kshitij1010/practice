# Singleton class Example


class SingletonClass:
    def __init__(self, c):
        self.c = c
        self._instance = None

    def __call__(self, *args, **kargs):
        if not self._instance:
            self._instance = self.c(*args, **kargs)
        return self._instance


@SingletonClass
class Calculation:
    def __init__(self):
        self.ans = 0

    def addition(self, *args):
        for num in args:
            self.ans += num
        return

    def subtraction(self, *args):
        for num in args:
            self.ans -= num
        return


a = Calculation()
a.addition(1,2,3,4)
b = Calculation()
print (a.ans)
print (b.ans)


b.addition(1)
print (a.ans)
print (b.ans)


a.subtraction(1, 2)
print (a.ans)
print (b.ans)
