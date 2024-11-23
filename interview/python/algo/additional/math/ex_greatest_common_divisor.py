# Example of greates common divisor
#
# GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is
# the largest number that divides both of them.
#
# https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/


def gcd(num1, num2):
    # everything divide zero
    if num2 == 0:
        return num1
    print (num2, num1%num2)
    return gcd(num2, num1%num2)


# print (gcd(56, 98)) # 14
#
print (gcd(18, 21)) # 3
# print (gcd(21, 18)) # 3
# print (gcd(-21, 18)) # 3
# print (gcd(-18, 21)) # 3
# print (gcd(-18, -21)) # -3
