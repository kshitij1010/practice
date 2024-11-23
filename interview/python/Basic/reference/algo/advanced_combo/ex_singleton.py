# Example of singleton class usng decorators
#
# Reference,
# https://www.youtube.com/watch?v=cGdkHbpoCuE

# singleton class (Using class method)

############## Second example ##############
class SingleTonClass:
    def __init__(self, c):
        self.c = c # here c is the class calling the singleton class
        self._instance = None # instance represents instance of the class, can be named anything

    def __call__(self, *args, **kargs): # need to have name __call__ to make it callable
        if not self._instance:
            self._instance = self.c(*args, **kargs)
        return self._instance


# helper class to call the singleton
@SingleTonClass # @ClassName, is the way to use the decorators
class MyClass():
    pass

a = MyClass()
b = MyClass()

a.name = "Test"
print ("a.name:",a.name, "\nb.name:", b.name) # should print "Test", same as a.name
b.num = 77
print ("\na.num:",a.num, "\nb.num:", b.num) # should print "77", same as b.name



############## Second example ( Addition > passing arguments using *args) ##############
@SingleTonClass
class AdditionClass():
    def __init__(self):
        self.sum = 0

    def addition(self, *args):
        for num in args:
            self.sum += num
        return


call1 = AdditionClass()
call1.addition(1,2,3,4)
call2 = AdditionClass()
print (call1.sum)
print (call2.sum)

call2.addition(1)
print (call1.sum)
print (call2.sum)


############## Third example ( FullName > passing defined arguments) ##############
@SingleTonClass
class FullName():
    def __init__(self):
        self.full_name = ""

    def get_name(self, first_name, last_name):
        self.full_name = first_name + last_name
        return


name_obj1 = FullName()
name_obj1.get_name("John", "Doe")
name_obj2 = FullName()
print (name_obj1.full_name)
print (name_obj2.full_name)

name_obj2.get_name("Kiara", "Adwani")
print (name_obj1.full_name)
print (name_obj2.full_name)
