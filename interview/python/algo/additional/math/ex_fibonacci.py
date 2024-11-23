# example of fibonacci sequence
# 0 1 1 2 3 5 8 13 21


def fibonacci(n):
    if n < 2:
        return n
    last_two = [0, 1]

    for i in range(1, n):
        last_two[0], last_two[1] = last_two[1], last_two[0]+last_two[1]

    return last_two[1]

print (fibonacci(5))



############## Follow up ########
# Given number, return the sum of fibonacci sequence nums up to n
#
# Example,
# Input: n = 1
# Output: 0
#
# Input: n = 2
# Output: 1

def fibonacci_sum(n):
    if n <= 1:
        return 0

    last_two = [0, 1]
    sum = last_two[0]
    for i in range(1, n):
        sum += last_two[1]
        last_two[0], last_two[1] = last_two[1], last_two[0]+last_two[1]

    return sum

print (fibonacci_sum(5)) # 7
