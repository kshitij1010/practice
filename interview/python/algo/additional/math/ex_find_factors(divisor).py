# Find all factors(divisor) of the given natural number
#
# https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/


def find_divisors(n):
    sqrt_n = int(n**(0.5))
    res = []
    for i in range(1, sqrt_n+1):
        if n%i == 0:
            divisor = n//i
            if divisor == i:
                res.append(i)
            else:
                res.append(i)
                res.append(divisor)

    return res


print (find_divisors(21))
