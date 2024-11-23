# LC70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# https://leetcode.com/problems/climbing-stairs/
# Eg-1,
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Eg-2,
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def ways_to_climb_steps(n, allowed_steps=[1,2]):
    if n < 0:
        return

    if n == 1 or n ==0:
        return n

    res = [0]*(n+1)
    res[0] = 1
    for i in range(1, n+1):
        total = 0
        for step in allowed_steps:
            if i-step >= 0:
                total += res[i-step]

        res[i] = total
    return res[-1]


print (ways_to_climb_steps(4, [1,3,5]))
print (ways_to_climb_steps(3))
