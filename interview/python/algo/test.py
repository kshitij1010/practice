# # Closest DashMart

# For questions or clarifications, please reach out to slack #eng-coding-interview-working-group and cc POC: John Ludwig


# # Problem Statement

# A DashMart is a warehouse run by DoorDash that houses items found in convenience stores, grocery stores, and restaurants. We have a city with open roads, blocked-off roads, and DashMarts. 

# City planners want you to identify how far a location is from its closest DashMart.

# You can only travel over open roads (up, down, left, right).

# Locations are given in `[row, col]` format.



# # Example 1

#     [
#     #     0    1    2    3    4    5    6    7    8    
#         ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'], # 0
#         ['X', ' ', 'X', 'X', 'C', ' ', ' ', ' ', 'X'], # 1
#         [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
#         [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
#         [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
#         [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']  # 5
#     ]

#     ' ' represents an open road that you can travel over in any direction (up, down, left, or right).
#     'X' represents an blocked road that you cannot travel through. 
#     'D' represents a DashMart.

#     # list of pairs [row, col]
#     locations = [
#         [200, 200],
#         [1, 4], 
#         [0, 3],
#         [5, 8],
#         [1, 8], 
#         [5, 5]    
#     ]
    
#     answer = [-1, 2, 0, -1, 6, 9]

#     Provided:
#     - city: char[][]
#     - locations: int[][2]

#     Return:
#     - answer: int[]


# Return a list of the distances from a given point to its closest DashMart. 


# Expected Answer: In this case, you should return `[-1, 2, 0, -1, 6, 9]`.

# # Example 2

#     [
#         ['D', 'X', 'X'],
#         ['D', 'D', 'X']
#     ]

#     locations = [[0, 2], [1, 1], [1, 2]]
#     answer = [-1, 0, 1]

def set_closest_dashmart_distances(city, locations):

    res = []
    for l in locations:
        row, col = l[0], l[1]
        
        visited = set()
        queue = []
        queue.append((row, col, 0))
        visited.add((row, col))
        temp = find_closest_dashmart(city, queue, visited, res, 1)
        res.append(temp)
    
    return res
    

def find_closest_dashmart(city, queue, visited, res, init):
    
    row, col, step = queue.pop(0)
    
    if row < 0 or col < 0 or row >= len(city) or col >= len(city[0]):
        return -1
    
    if city[row][col] == 'X' and init != 1:
        return -1
    
    if city[row][col] == 'D':
        return step
    
    init = 0
    visited.add((row, col))
    for r,c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if (r,c) not in visited:
            queue.append((r, c, step+1))
    
    temp_res = -1
    while queue:
        temp_res = max(temp_res, find_closest_dashmart(city, queue, visited, res, init))

    return temp_res

    
'''
1st call: 
q:  (0,3, 2), ()
c:  (0,4) ------ 


res = [2, ]
'''

    
def test_example_1():
    city = [
    #     0    1    2    3    4    5    6    7    8
        ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'], # 0
        ['X', ' ', 'X', 'X', 'C', ' ', ' ', ' ', 'X'], # 1
        [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
        [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
        [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
        [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']  # 5
    ]

    locations = [
        [200, 200],
        [1, 4],
        [0, 3],
        [5, 8],
        [1, 8],
        [5, 5]
    ]
    
    expected_answer = [-1, 2, 0, -1, 6, 9]
    result = set_closest_dashmart_distances(city, locations)
    print(result)
    assert result == expected_answer
    

def test_example_2():
    city = [
        ['D', 'X', 'X'],
        ['D', 'D', 'X']
    ]

    locations = [[0, 2], [1, 1], [1, 2]]

    expected_answer = [-1, 0, 1]
    result = set_closest_dashmart_distances(city, locations)
    print (result)
    assert result == expected_answer
    
def test_no_dashmarts():
    city = [
        # 0,   1,   2,   3,   4,   5,   6,   7,   8
        [' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' '], # 0
        ['X', 'X', 'X', ' ', ' ', 'X', ' ', ' ', 'X'], # 1
    ]
    locations = [[0, 3], [0, 5], [1, 8]]
    expected_answer = [-1, -1, -1]
    result = set_closest_dashmart_distances(city, locations)
    print (result)
    assert result == expected_answer


test_example_1()
test_example_2()
test_no_dashmarts()    
