# Least common multiple
#
# LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers.
# For example LCM of 15 and 20 is 60 and LCM of 5 and 7 is 35.
# For example GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.
#
# https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
# https://www.geeksforgeeks.org/program-to-find-lcm-of-2-numbers-without-using-gcd/

def gcd(num1, num2):
    if num2 == 0:
        return num1

    return gcd(num2, num1%num2)

def find_lcm(num1, num2):
    return int(num1*num2/gcd(num1, num2))


print (find_lcm(15, 20))
