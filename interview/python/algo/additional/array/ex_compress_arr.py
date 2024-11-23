# given a sorted array compress it
# Eg, 
# [1,2,3,5,7,8,9] -> ['1-3', 5, '7-9']
# [1,3,5,7,15,18,21] -> ['1-7x2', '15-21x3']
# [1,2] -> [1, 2]
# [] -> []
# [0,5,10,18,21,22,23] -> ['0-10x5', 18, '21-23']
# [1,5,8,12,23,45,56] -> [1, 5, 8, 12, 23, 45, 56]
# [1,5,8,20,55,222,701] -> [1, 5, 8, 20, 55, 222, 701]
# [0,4,5,6,7,9,21,22,23]-> [0, '4-7', 9, '21-23']


def shorty(nums):
	len_arr = len(nums)
	if len(nums) <= 2:
		return nums

	nums.sort()

	res = []
	diff = float('-inf')
	i = 0
	while i < len_arr:
		prev = i

		while (prev + 1 < len_arr) and (nums[prev + 1] - nums[prev] ==  diff):
			prev += 1

		if prev-i <= 1:
			if diff == float('-inf') and prev + 1 < len_arr:
				diff = nums[prev+1] - nums[prev]
				continue
			res.append(nums[i])
			i += 1
		else:
			s = str(nums[i]) + "-" + str(nums[prev])
			if diff > 1:
				s += "x" + str(diff)
			res.append(s)
			i = prev + 1
		diff = float('-inf')
	
	return res


test1 = [1,2,3,5,7,8,9]
print (shorty(test1))


test2 = [1,3,5,7,15,18,21]
print (shorty(test2))


test3 = [1,2]
print (shorty(test3))


test4 = []
print (shorty(test4))

test5 = [0,5,10,17,21,24,27]
print (shorty(test5))


test6 = [1,5,8,12,23,45,56]
print (shorty(test6))


test7 = [1,5,8,20,55,222,701]
print (shorty(test7))


test8 = [0,4,5,6,7,9,21,22,23]
print (shorty(test8))

test9 = [0,4,5,6,7,9,21,22,23,57]
print (shorty(test9))
