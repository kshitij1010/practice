# 10. move zeros to the left
# Given an integer array, move all elements that are 0 to the left while maintaining the order of other elements in the array. The array has to be modified in-place. Try it yourself before reviewing the solution and explanation.

def move_zeros_to_left(arr):
    if arr is None or len(arr) == 0:
        return arr

    read = len(arr)-1
    write = len(arr)-1

    while read >= 0:
        if arr[read] == 0:
            read -= 1
            continue
        arr[read], arr[write] = arr[write], arr[read]
        read -= 1
        write -= 1

    return arr



data = [
        {
            "input": [1, 10, 20, 0, 23, 23, 0, 88, 0], 
            "output": [0, 0, 0, 1, 10, 20, 23, 23, 88],
        },
        {
            "input": [0, 0, 0, 0], 
            "output": [0, 0, 0, 0],
        },
        {
            "input": [0, 0, 0, 0, 1], 
            "output": [0, 0, 0, 0, 1],
        },
        {
            "input": [1, 23, 5, 57, 72], 
            "output": [1, 23, 5, 57, 72],
        },
    ]


from helper import Test
test = Test()
test.check(move_zeros_to_left, data)
