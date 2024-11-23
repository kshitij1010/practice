# Link: https://leetcode.com/problems/two-sum


from helper import Test


# Solution
def twoSum(self, nums: list[int], target: int) -> list[int]:
    index_list = {}
    
    for i, n in enumerate(nums):
        if n in index_list:
            return [index_list[n],i]
        index_list[target - n] = i
        
    return []



# Start test
data = [
        {
            "input": [[2,7,11,15], 9], 
            "output": [0,1],
        },
        {
            "input": [[3,2,4], 6], 
            "output": [1,2],
        },
        {
            "input": [[3,3], 6], 
            "output": [0,1],
        }
    ]


# Start test
test = Test()
test.check(twoSum, data)
