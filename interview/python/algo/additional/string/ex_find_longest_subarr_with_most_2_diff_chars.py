# Find the longest subarr with at most 2 different chars

# Similar example:
# https://leetcode.com/problems/fruit-into-baskets/solution/
# Complexity Analysis
# Time Complexity: O(N)O(N), where NN is the length of tree.
# Space Complexity: O(N)O(N).


def longest_subarr_with_at_most_two_diff_chars(arr):
    if len(arr) == 0 or arr is None:
        return 0

    l = 0
    char_count = {}
    longest_subrarr = 0

    for r in range(len(arr)):
        if arr[r] in char_count:
            char_count[arr[r]] += 1
        else:
            char_count[arr[r]] = 1

        while len(char_count) > 2:
            char_count[arr[l]] -= 1
            if not char_count[arr[l]]:
                char_count.pop(arr[l])
            l += 1

        longest_subrarr = max(longest_subrarr, r-l+1)

    return longest_subrarr


print(longest_subarr_with_at_most_two_diff_chars(["a", "b", "a", "a", "c"])) # 4
print(longest_subarr_with_at_most_two_diff_chars(["a", "b", "a", "b", "c"])) # 4
print(longest_subarr_with_at_most_two_diff_chars(["a", "b", "a", "c", "a"])) # 3
