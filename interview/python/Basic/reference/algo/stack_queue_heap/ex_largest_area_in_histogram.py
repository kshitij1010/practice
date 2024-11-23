# Count the max area of rectangular in histogram


def max_area_rect_in_histogram(arr):
    if len(arr) == 0 or arr is None:
        return

    if len(arr) == 1:
        return arr[0]

    stack = []
    arr_size = len(arr)
    i = 0
    area = 0
    max_area = float('-inf')

    while i < arr_size:
        if len(stack) == 0 or arr[i] >= arr[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            poped_val = stack.pop()

            if len(stack) == 0:
                area = arr[poped_val] * i
            else:
                area = arr[poped_val] * (i- stack[-1] - 1)
            max_area = max(max_area, area)


    while len(stack) > 0:
        poped_val = stack.pop()

        if len(stack) == 0:
            area = arr[poped_val] * i
        else:
            area = arr[poped_val] * (i - stack[-1] - 1)
        max_area = max(max_area, area)


    return max_area


print (max_area_rect_in_histogram([1,3,5,3,2,1])) # 9
print (max_area_rect_in_histogram([1,2,3,4,3])) # 9
print (max_area_rect_in_histogram([6,2,5,4,5,1,6])) # 12
