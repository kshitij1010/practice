# Write a program to reverse an array or string

# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/


def reverse_arr(arr):
    if len(arr) == 0 or arr is None:
        raise Exception("Invalid input!!!!!")

    low = 0
    high = len(arr) - 1

    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

    return



arr1 = [1, 2, 3, 4, 5]
print ("Orig1:", arr1)
reverse_arr(arr1)
print ("Reversed:", arr1)

arr2 = [8, 8, 8, 7]
print ("Orig2:", arr2)
reverse_arr(arr2)
print ("Reversed2:", arr2)

arr3 = ['a', 'b', 'c', 'd']
print ("Orig3:", arr3)
reverse_arr(arr3)
print ("Reversed3:", arr3)

arr4 = [8, 8, 8, 7] + ['a', 'b', 'c', 'd']
print ("Orig4:", arr4)
reverse_arr(arr4)
print ("Reversed4:", arr4)

# reverse_arr("") # exception will be raised
