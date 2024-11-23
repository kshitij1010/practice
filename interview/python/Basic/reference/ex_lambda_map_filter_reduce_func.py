##################### Lambda #####################
print ("##################### Lambda Example #####################")
###### Example 1: return the double of the input
## normal function
def double_num(x):
    return x*2
## Lambda function
double = lambda x: x*2
## test
print ("\nExample 1,\nNormal function, double_num(5):", double_num(5))
print ("Lambda function, double(5):", double(5))
print ("Normal function, double_num(777):", double_num(777))
print ("Lambda function, double(777):", double(777))

###### Example 2: return the sum/addition of two numbers
## normal function
def add(x, y):
    return x+y
## Lambda function
addition = lambda x,y: x+y
## test
print ("\nExample 2,\nNormal function, add(5, -1):", add(5, -1))
print ("Lambda function, addition(5, -1):", addition(5, -1))
print ("Normal function, add(77.60, 22.40):", add(77.60, 22.40))
print ("Lambda function, addition(77.60, 22.40):", addition(77.60, 22.40))


###### Example 3: return max of two numbers
## normal function
def find_max(x, y):
    if x > y:
        return x
    return y
## Lambda function
maximum = lambda x,y: x if x > y else y
## test
print ("\nExample 3,\nNormal function, find_max(5, -1):", find_max(5, -1))
print ("Lambda function, maximum(5, -1):", maximum(5, -1))
print ("Normal function, find_max(77.60, 22.40):", find_max(77.60, 22.40))
print ("Lambda function, maximum(77.60, 22.40):", maximum(77.60, 22.40))




##################### Map #####################
print ("\n\n##################### Map #####################")
###### Example 1: square of each element in the array
## normal function
def square(arr):
    res = []
    for i in arr:
        res.append(i**2)
    return res

## test
n = [4, 3, 2, 1]
n1 = [10, 20, 30]
print ("Input:n=", n, "and n1=", n1)
print ("\nExample 1,\nNormal function, square(n):", square(n))
print ("Normal function, square(n1):", square(n1))
## Map function
print ("Map function: print (list(map(lambda x: x**2, n))) or (list(map(square1, n)))")
ans = list(map(lambda x: x**2, n))
print ("Map function:", ans)

# map function using another def function
def square1(i):
    return i**2
ans = list(map(square1, n1))
print ("Map function:", ans)




##################### Filter #####################
print ("\n\n##################### Filter #####################")
###### Example 1:
## normal function
def greater_than_five(arr):
    res = []
    for i in arr:
        if i > 5:
            res.append(i)
    return res

## test
n = [4, 7, 3, 9, 2, 1, 87]
print ("Input:", n)
print ("\nExample 1,\nNormal function, greater_than_five(n):", greater_than_five(n))
# Filter function using lambda function
ans = list(filter(lambda x: x > 5, n))
print ("Filter function: list(filter(lambda x: x > 5, n)):", ans)
# Filter function using another def function
def greater_than_five1(i):
    if i > 5:
        return i
    return
ans = list(filter(greater_than_five1, n))
print ("Filter function:", ans)

###### Example 2: remove the none value
names = ["John", "Lisa", None, "abc", "Will", None, None, None, "Scarlet", None, "Alexa"]
print ("\nExample 2,\nInput: ", names)
new_ans = list(filter(None, names))
print ("Filter function to remove the None ( new_ans = list(filter(None, names)) ):", new_ans)





##################### Reduce #####################
print ("\n\n##################### Reduce #####################")

from functools import reduce

###### Example 1:
## normal function
def product_of_arr(arr):
    res = arr[0]
    for i in range(1,len(arr)):
        res *= arr[i]
    return res

## test
n = [4, 7, 3, 9, 2, 1, 87]
print ("Input:", n)
print ("\nExample 1,\nNormal function, product_of_arr(n):", product_of_arr(n))
# Filter function using lambda function
multiplier = lambda x, y: x * y
ans = reduce(multiplier, n)
print ("Reduce function: list(reduce(lambda x, y: x * y, n)) or reduce(multiplier, n) where (multiplier = lambda x, y: x * y):", ans)
