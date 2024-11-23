# Given a list of float numbers, insert “+”, “-”, “*” or “/” between each consecutive pair of numbers
# to find the maximum value you can get.
# For simplicity, assume that all operators are of equal precedence order and evaluation happens from left to right.
# Example:
#
# (1, 3, 4) -> (1 + 4) * 3  = 16
#
# (1, 12, -3) -> (-1 - 12) * -3  = 39
#
# (2, 0, 9) -> 2 * (0 + 9)  = 18
# float getMaxNumber(float[] nums)...



def get_max_after_calculation(nums):
    maximum = 0
    minimum = 0

    for i in nums:
        a1 = max(minimum+i, maximum+i)
        a2 = min(minimum-i, maximum-i)
        a3 = max(minimum*i, maximum*i)
        if i != 0:
            a4 = min(minimum//i, maximum//i)
        else:
            a4 = 0
        maximum = max(a1,a2,a3,a4)
        minimum = min(a1,a2,a3,a4)
    return max(minimum, maximum)


arr1 = [1,3,4]
print (get_max_after_calculation(arr1))

arr2 = [1,12,-3]
print (get_max_after_calculation(arr2))

arr3 = [1,12,3]
print (get_max_after_calculation(arr3))

arr4 = [2,0,9]
print (get_max_after_calculation(arr4))

arr5 = [-1,-3,-4]
print (get_max_after_calculation(arr5))

arr6 = [0,0,0]
print (get_max_after_calculation(arr6))
