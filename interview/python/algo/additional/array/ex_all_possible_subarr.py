# Print all the subset of the array
# Print all the combination of the array

def all_subsets(arr, curr_ind, curr, res):
    n = len(arr)

    if curr_ind == n:
        res.append(curr)
        return

    # Two cases for every character
    # (i) We consider the character as part of current subset
    all_subsets(arr, curr_ind+1, curr+[arr[curr_ind]], res)
    # (ii) We do not consider current character as part of current subset
    all_subsets(arr, curr_ind+1, curr, res)


def find_all_subsets(arr):
    res = []
    all_subsets(arr, 0, [], res)
    return res

print (find_all_subsets(["a", "b", "c"]))
