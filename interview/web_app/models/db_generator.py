import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Questions

db_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "quesions.db")
db_uri = 'sqlite:///{}'.format(db_dir)
engine = create_engine(db_uri)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


questions = [
    {
        "name": "Find max aggregate Profit",
        "descriptions": "You are given an array.<br>Find the maximum profit you can\n\n\n \
                        get by summing the element of array.\n\
                        Only constrain is that you cannot include two neighbor elements in the sum.",
        "example": "1.) Input: [2, 8, 3, 50, 7, 1]<br>Output: 59        <= (8 + 50 + 1)",
        "reference": "",
    },
    {
        "name": "All combinations",
        "descriptions": "Print all the subset of the array<br>Print all the combination of the array",
        "example": "",
        "reference": "",
    },
    {
        "name": "All arith operations",
        "descriptions": "Given a list of float numbers, \
                        insert “+”, “-”, “*” or “/” between each consecutive \
                        pair of numbers<br>to find the maximum value you can get.<br>\
                        For simplicity, assume that all operators are of equal precedence \
                        order and evaluation happens from left to right.",
        "example": "1.) (1, 3, 4) -> (1 + 4) * 3  = 16<br>2.) (1, 12, -3) -> (-1 - 12) * -3  = 39",
        "reference": "",
    },
    {
        "name": "Contiguous binary subarr",
        "descriptions": "Given a binary array, \
                        find the maximum length of a contiguous subarray with equal number of 0 and 1.",
        "example": "1.) Input: [0,1,0]<br>Output: 2<br>Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.",
        "reference": "https://leetcode.com/problems/contiguous-array/",
    },
    {
        "name": "Getting a Different Number (From pramp)",
        "descriptions": "Given an array arr of unique nonnegative integers,\
                        implement a function getDifferentNumber that finds the smallest\
                        nonnegative integer that is NOT in the array.<br>\
                        Even if your programming language of choice doesn’t have that restriction (like Python),\
                        assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance,\
                        the operation MAX_INT + 1 would be undefined in our case.<br>\
                        Your algorithm should be efficient, both from a time and a space complexity perspectives.<br>\
                        ",
        "example": "1.) Input:  arr = [0, 1, 2, 3]<br>Output: 4",
        "reference": "https://www.pramp.com/challenge/aK6V5GVZ9MSPqvG1vwQp",
    },
    {
        "name": "Island count",
        "descriptions": "Count the island in the given matrix. Vertically and horizontally connected 1s make an island.",
        "example": "1.) [ [0,    1,    0,    1,    0],<br>\
                         [0,    0,    1,    1,    1],<br>\
                         [1,    0,    0,    1,    0],<br>\
                         [0,    1,    1,    0,    0],<br>\
                         [1,    0,    1,    0,    1] ]<br>Output: 6",
        "reference": "",
    },
    {
        "name": "K-Messed Array Sort",
        "descriptions": "Given an array of integers arr where each element is at most k \
                        places away from its sorted position,<br>\
                        code an efficient function sortKMessedArray that sorts arr.<br>\
                        For instance, for an input array of size 10 and k = 2,<br>\
                        an element belonging to index 6 in the sorted array will be\
                         located at either index 4, 5, 6, 7 or 8 in the input array.",
        "example": "1.) Input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2<br>output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
        "reference": "https://www.pramp.com/challenge/XdMZJgZoAnFXqwjJwnBZ",
    },
    {
        "name": "Knapsack Problem | DP",
        "descriptions": "Given weights and values of n items,\
                        put these items in a knapsack of capacity W to get the maximum total value in the knapsack.<br>\
                        In other words, given two integer arrays val[0..n-1] and wt[0..n-1]\
                        which represent values and weights associated with n items respectively.<br>\
                        Also given an integer W which represents knapsack capacity,\
                        find out the maximum value subset of val[]\
                        such that sum of the weights of this subset is smaller than or equal to W.<br>\
                        You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/",
    },
    {
        "name": "Area in histogram",
        "descriptions": "Count the max area of rectangular in histogram",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=RVIh0snn4Qc",
    },
    {
        "name": "Largest square in Matrix",
        "descriptions": "Find the largest square of 1's in 2d matrix.",
        "example": "1.) 1 1 0 1 0<br>\
                    0 1 1 1 0<br>\
                    1 1 1 1 0<br>\
                    0 1 1 1 0<br>Output: 3 (since 3X3 is the largest square in this matrix)",
        "reference": "https://www.youtube.com/watch?v=FO7VXDfS8Gk",
    },
    {
        "name": "Longest increasing subsequence with the highest sum",
        "descriptions": "Find the Longest increasing subsequencewith the highest sum",
        "example": "1.) Input: [4, 6, 1, 3, 8, 4, 6]<br>Output: [4, 6, 8] (sums to  18 which is the highest sum)",
        "reference": "https://www.youtube.com/watch?v=99ssGWhLPUE",
    },
    {
        "name": "Find the Longest Increasing Subsequence",
        "descriptions": "Given an array of numbers, find the length of the longest increasing subsequence in the array.<br>\
                        The subsequence does not necessarily have to be contiguous.",
        "example": "1.) Input: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]<br>\
                    Output: 6 (Explanation: the increasing arr is 0, 2, 6, 9, 11, 15)",
        "reference": "",
    },
    {
        "name": "Matrix product",
        "descriptions": "Given a matrix, find the path from top left to bottom right with the greatest product by moving only down and right.",
        "example": "1.) [[1, 2, 3]<br>\
                        [4, 5, 6]<br>\
                        [7, 8, 9]<br>Output: 2016 (Explanation: 1 -> 4 -> 7 -> 8 -> 9)",
        "reference": "https://www.byte-by-byte.com/matrixproduct/",
    },
    {
        "name": "Matrix Spiral",
        "descriptions": "Given a 2D array (matrix) inputMatrix of integers,<br>\
                        create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise.<br>\
                        Your function then should return that array.",
        "example": "1.) input:  inputMatrix  = [ [1,    2,   3,  4,    5], <br> \
                                 [6,    7,   8,  9,   10], <br> \
                                 [11,  12,  13,  14,  15], <br> \
                                 [16,  17,  18,  19,  20] ] <br> \
                                 output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]",
        "reference": "",
    },
    {
        "name": "Median of Array",
        "descriptions": "Find the median of two sorted arrays.",
        "example": "1.) arr1 = [1, 3, 5], arr2 = [2, 4, 6]<br>median(arr1, arr2) = 3.5",
        "reference": "https://www.youtube.com/watch?v=LPFhl65R7ww",
    },
    {
        "name": "Min conference room",
        "descriptions": "Given an array of meeting time intervals consisting of start and end times.[[s1,e1],[s2,e2],...] (si < ei),<br>\
                        find the minimum number of conference rooms required.",
        "example": "1.) Given [[0, 30],[5, 10],[15, 20]],<br>return 2",
        "reference": "",
    },
    {
        "name": "Number of Paths in Matrix",
        "descriptions": "Count number of ways to reach destination in a Maze<br>\
                        Given a maze with obstacles,<br>\
                        count number of paths to reach rightmost-bottommost cell from topmost-leftmost cell.<br>\
                        A cell in given maze has value -1 if it is a blockage or dead end, else 0.",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/count-number-ways-reach-destination-maze/",
    },
    {
        "name": "Rotate array",
        "descriptions": "Given an array, rotate the array to the right by k steps, where k is non-negative.",
        "example": "https://leetcode.com/problems/rotate-array/",
        "reference": "https://www.youtube.com/watch?v=8kyZPizZzWc",
    },
    {
        "name": "Ways to climb",
        "descriptions": "Given N steps, and possible jump; how many ways we can reach to N stepss",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=5o-kdjv7FD0",
    },
    {
        "name": "Stock Profit",
        "descriptions": "Write an efficient function that takes stock_prices and<br>\
                        returns the best profit I could have made from one purchase \
                        and one sale of one share of Apple stock yesterday.<br>\
                        ",
        "example": "1.) stock_prices = [10, 7, 5, 8, 11, 9]<br>Returns 6 (buying for $5 and selling for $11)",
        "reference": "https://www.interviewcake.com/question/python/stock-price",
    },
    {
        "name": "Maximum size rectangle binary sub-matrix with all 1s",
        "descriptions": "Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s.",
        "example": "1.) <br>0 1 1 0<br>\
                    1 1 1 1<br>\
                    1 1 1 1<br>\
                    1 1 0 0<br>Output: 8 (since 2X4 is the largest rectangle in this matrix)",
        "reference": "https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/",
    },
    {
        "name": "Permutation of a string",
        "descriptions": "Write a recursive function for generating all permutations of an input string.",
        "example": "1.) Input: 'ab'<br> Output:['ab', 'ba']",
        "reference": "https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/",
    },
    {
        "name": "Longest Substring with most 2 unique char",
        "descriptions": "Find the longest subarr with at most 2 different chars.",
        "example": "",
        "reference": "https://leetcode.com/problems/fruit-into-baskets/solution/",
    },
    {
        "name": "Palindromic Partition",
        "descriptions": "Given a string, print all possible palindromic partitions.<br>https://statyang.wordpress.com/python-practice-83-palindrome-partitioning/",
        "example": "1.) Input   : 'nitin'<br>\
                        Output  : n i t i n<br>\
                                  n iti n<br>\
                                  nitin",
        "reference": "https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/",
    },
    {
        "name": "Longest common subsequence",
        "descriptions": "Find longest common subsequence of given two strings",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/printing-longest-common-subsequence/",
    },
    {
        "name": "Longest common substring",
        "descriptions": "Find longest common subsequence of given two strings.",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=BysNXJHzCEs",
    },
    {
        "name": "Longest Substring Without Repeating Characters",
        "descriptions": "Check example",
        "example": "1.) Input: 'pwwkew'<br>\
                        Output: 'wke'<br>\
                        Explanation: The answer is 'wke', with the length of 3.\
                        Note that the answer must be a substring, 'pwke' is a subsequence and not a substring.",
        "reference": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
    },
    {
        "name": "Basic Regex Parser",
        "descriptions": "Regex match",
        "example": "1.) input:  text = 'acd', pattern = 'ab*c.'",
        "reference": "https://www.youtube.com/watch?v=l3hda49XcDE",
    },
    {
        "name": "Wildcard match",
        "descriptions": "Wildcard Match",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=3ZDZ-N0EPV0",
    },
    {
        "name": "Reverse Words",
        "descriptions": "Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.",
        "example": "message = [ 'c', 'a', 'k', 'e', ' ',\
                    'p', 'o', 'u', 'n', 'd', ' ',\
                    's', 't', 'e', 'a', 'l' ]",
        "reference": "https://www.interviewcake.com/question/python/reverse-words?course=fc1&section=array-and-string-manipulation",
    },
    {
        "name": "Binary Tree Level Order Traversal",
        "descriptions": "Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).",
        "example": "Given binary tree [3,9,20,null,null,15,7],<br>\
                        3<br>\
                       / \<br>\
                      9  20<br>\
                        /  \<br>\
                       15   7<br>\
                       Output:[[3],[9,20],[15,7]]",
        "reference": "",
    },
    {
        "name": "Find num of unival sub tree",
        "descriptions": "Counting Unival Subtrees / Find Count of Single Valued Subtrees<br>\
                        Given a binary tree, write a program to count the number of Single Valued Subtrees.<br>\
                        A Single Valued Subtree is one in which all the nodes have same value.<br>\
                        Expected time complexity is O(n).",
        "example": "",
        "reference": "https://www.dailycodingproblem.com/blog/unival-trees/",
    },
    {
        "name": "Minimal Tree",
        "descriptions": "Given a sorted (increasing order) array with unique interger elements,\
                        write an algorithm to creat a binary search tree with minimal height",
        "example": "CTCI trr_n_graph #ex2",
        "reference": "",
    },
    {
        "name": "In Order Successor",
        "descriptions": "Find the inorder successor in the given tree",
        "example": "",
        "reference": "",
    },
    {
        "name": "Largest Smaller BST Key",
        "descriptions": "Given a root of a Binary Search Tree (BST) and a number num,<br>\
                        implement an efficient function findLargestSmallerKey<br>\
                        that finds the largest key in the tree that is smaller than num.<br>\
                        If such a number doesn’t exist, return -1.<br>\
                        Assume that all keys in the tree are nonnegative.",
        "example": "1.) For num = 17 and the binary search tree below:\
                                    7<br>\
                                /        \<br>\
                              3          10<br>\
                            /  \       /     \<br>\
                           1   5      8      15<br>\
                                       \    /    \<br>\
                                       9   12    17<br>\
                        Your function would return:<br>\
                        15 since it’s the largest key in the tree that is still smaller than 17.",
        "reference": "",
    },
    {
        "name": "Longest consequetive seq",
        "descriptions": "Longest consecutive sequence in Binary tree.<br>\
                        Given a Binary Tree find the length of the longest path\
                        which comprises of nodes with consecutive values in increasing order.\
                        Every node is considered as a path of length 1.",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/longest-consecutive-sequence-binary-tree/",
    },
    {
        "name": "Tree Example",
        "descriptions": "TREE example:<br>\
                        1. find the max height of the tree<br>\
                        2. find the min height of the tree<br>\
                        3. check if the given binary tree is binary search tree(BST) or not<br>\
                        4. print leaf node<br>\
                        5. print full node<br>\
                        6. print Pre-order, In-order, Post-order<br>\
                        7. print all the route from root node to leaf node<br>\
                        8. print all the node of the route with the max height of the tree",
        "example": "",
        "reference": "",
    },
    {
        "name": "LRU cache",
        "descriptions": "Basic implmentation if LRU.",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=R0GTqg3pJKg",
    },
    {
        "name": "Animal Shelter",
        "descriptions": "Design Animal shelter class with adopt and drop functionalities.",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=R0GTqg3pJKg",
    },
    {
        "name": "N Queens",
        "descriptions": "place N queens so that none of the queen attacks each other in NxN chess board.",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=jJPtLzq1E-Y",
    },
    {
        "name": "Singleton",
        "descriptions": "Example of singleton class usng decorators.",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=cGdkHbpoCuE",
    },
    {
        "name": "Autocomplete/word search",
        "descriptions": "Write a method to get autocompletion job for the given word. Dictionary is also given as in argument",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=o6563NNbdtg&feature=youtu.be",
    },
    {
        "name": "BFS/DFS",
        "descriptions": "Basic code example of BFS and DFS",
        "example": "https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/",
        "reference": "https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/",
    },
    {
        "name": "Binary Search",
        "descriptions": "Binary search for the sorted array (Implement iterative Binary Search.)",
        "example": "",
        "reference": "",
    },
    {
        "name": "Heap Sort",
        "descriptions": "Example of heap_sort",
        "example": "",
        "reference": "",
    },
    {
        "name": "Merge sort",
        "descriptions": "Example of merge_sort",
        "example": "Algorithmic Paradigm: Divide and Conquer",
        "reference": "",
    },
    {
        "name": "Quick sort",
        "descriptions": "Example of quick_sort",
        "example": "",
        "reference": "",
    },
    {
        "name": "Acyclic?",
        "descriptions": "Find if given directed graph has a cycle or not",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=rGaJgYS456c",
    },

    {
        "name": "Queue using stack",
        "descriptions": "Implment queue using stack",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=n1nsfg8O4Mk",
    },
    {
        "name": "Stack using queue",
        "descriptions": "Implment stack using queue",
        "example": "",
        "reference": "https://www.youtube.com/watch?v=xBugrptVRUQ",
    },
    {
        "name": "Triple to Sum",
        "descriptions": "Count triplets with sum smaller than a given value<br>\
                        Given an array of distinct integers and a sum value.<br>\
                        Find count of triplets with sum smaller than given sum value.\
                        Expected Time Complexity is O(n2).",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/",
    },
    {
        "name": "Zigzag",
        "descriptions": "Convert array into Zig-Zag fashion<br>\
                        Given an array of DISTINCT elements,<br>\
                        rearrange the elements of array in zig-zag fashion in O(n) time.<br>\
                        The converted array should be in form a < b > c < d > e < f.",
        "example": "1.) Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}<br>Output: arr[] = {3, 7, 4, 8, 2, 6, 1}<br>\
                    2.) Input:  arr[] =  {1, 4, 3, 2}<br>Output: arr[] =  {1, 4, 2, 3}",
        "reference": "https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/",
    },
    {
        "name": "Largest array with contiguous elems",
        "descriptions": "Length of the largest subarray with contiguous elements<br>\
                        Given an array of distinct integers,<br>\
                        find length of the longest subarray which contains numbers that can be arranged in a continuous sequence.",
        "example": "1.) Input:  arr[] = {10, 12, 11}; Output: Length of the longest contiguous subarray is 3<br>\
                    2.) Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45}; Output: Length of the longest contiguous subarray is 5",
        "reference": "https://www.geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-1/",
    },
    {
        "name": "Shortest path in undirected Graph",
        "descriptions": "Find shortest path between 2 nodes in undirected graph",
        "example": "",
        "reference": "https://www.interviewcake.com/question/python/mesh-message?course=fc1&section=trees-graphs",
    },
    {
        "name": "Merge_meeting_numbers",
        "descriptions": "Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.",
        "example": "1.) Input:  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]<br>\
                    Output: [(0, 1), (3, 8), (9, 12)]",
        "reference": "https://www.interviewcake.com/question/python/reverse-words?course=fc1&section=array-and-string-manipulation",
    },
    {
        "name": "All unique char",
        "descriptions": "Is Unique: Implement an algorithm to determine if a string has all unique characters.",
        "example": "",
        "reference": "CITC - arr_string 1",
    },
    {
        "name": "Check permutation",
        "descriptions": "Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.",
        "example": "",
        "reference": "CITC - arr_string 2",
    },
    {
        "name": "Palindrome permutation",
        "descriptions": "Given a string, write a function to check if it is a permutation of a palin- drome.",
        "example": "",
        "reference": "CITC - arr_string 4",
    },
    {
        "name": "One way",
        "descriptions": "There are three types of edits that can be performed on strings:\
                        insert a character, remove a character, or replace a character.\
                        Given two strings, write a function to check if they are one edit (or zero edits) away.",
        "example": "1.) pale, ple -> true <br>2.) pale, bake -> false <br>3.) pale, bale -> true",
        "reference": "CITC - arr_string 5",
    },
    {
        "name": "String Rotation",
        "descriptions": "Assume you have a method isSubstring which checks ifone word is asubstring of another.<br>\
                        Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring",
        "example": "'waterbottle' is a rotation of 'erbottlewat'",
        "reference": "CITC - arr_string 9",
    },
    {
        "name": "Return Kth to Last",
        "descriptions": "Implement an algorithm to find the kth to last element of a singly linked list.",
        "example": "",
        "reference": "CITC - linked lsit 2",
    },
    {
        "name": "Linked List Partition",
        "descriptions": "Write code to partition a linked list around a value x, such that all nodes less than x come \
                        before all nodes greater than or equal to x. <br> \
                        If x is contained within the list, the values of x only need \
                        to be after the elements less than x (see below). The partition element x can appear anywhere in the \
                        right partition; it does not need to appear between the left and right partitions.",
        "example": "1.) Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]<br> Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8",
        "reference": "CITC - linked lsit 4",
    },
    {
        "name": "Sum Lists",
        "descriptions": "You have two numbers represented by a linked list, where each node contains a single \
                        digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. \
                        Write a function that adds the two numbers and returns the sum as a linked list.<br>\
                        FOLLOW UP<br>\
                        Suppose the digits are stored in forward order. Repeat the above problem.",
        "example": "1.) Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.<br>Output: 2 -> 1 -> 9. That is, 912.",
        "reference": "CITC - linked lsit 5",
    },
    {
        "name": "Palindrome Linked List",
        "descriptions": "Implement a function to check if a linked list is a palindrome.",
        "example": "",
        "reference": "CITC - linked lsit 6",
    },
    {
        "name": "Linked List Intersect",
        "descriptions": "Given two (singly) linked lists, determine if the two lists intersect.<br>\
                        Return the intersecting node.<br>\
                        Note that the intersection is defined based on reference, not value.",
        "example": "",
        "reference": "CITC - linked lsit 7",
    },
    {
        "name": "Loop Detection",
        "descriptions": "Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop",
        "example": "1.) Input: A -> B -> C -> D -> E -> C [the same C as earlier]<br> Output: C",
        "reference": "CITC - linked lsit 8",
    },
    {
        "name": "Route between Nodes",
        "descriptions": "Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.",
        "example": "",
        "reference": "CITC - tree n graph 1",
    },
    {
        "name": "Check Balanced Tree",
        "descriptions": "Implement a function to check if bianry tree is banalanced. \
                        A Balanced tree is defined to be a tree \
                        such that the height of the two subtrees of any node never differ by more than one.",
        "example": "",
        "reference": "CITC - tree n graph 4",
    },
    {
        "name": "Insert into a Binary Search Tree",
        "descriptions": "Given the root node of a binary search tree (BST) and a value to be inserted into the tree,<br>\
                        insert the value into the BST. Return the root node of the BST after the insertion.<br>\
                        It is guaranteed that the new value does not exist in the original BST.<br><br>\
                        Note that there may exist multiple valid ways for the insertion,\
                        as long as the tree remains a BST after insertion. You can return any of them.",
        "example": "",
        "reference": "https://leetcode.com/problems/insert-into-a-binary-search-tree/",
    },
    {
        "name": "Reverse LinkedList",
        "descriptions": "Given linkedlist, reverse it without using additional space. Time complexity: O(n), space complexity: O(1)",
        "example": "",
        "reference": "https://leetcode.com/problems/reverse-linked-list/",
    },
    {
        "name": "Longest path between 2 vertices (max sum of the path between any two vertices)",
        "descriptions": "Given an undirected graph. Find the max sum of the weight between any 2 vertices.<br><br>\
                        We are given a map of cities connected with each other via cable lines such that \
                        there is no cycle between any two cities.<br>\
                        We need to find the maximum length of cable between any two cities for given city map.",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/longest-path-between-any-pair-of-vertices/",
    },
    {
        "name": "Different views of tree",
        "descriptions": "Given a tree, print the left view, right view, top view, bottom view.",
        "example": "https://www.geeksforgeeks.org/print-right-view-binary-tree-2/ <br>\
                    https://www.geeksforgeeks.org/print-left-view-binary-tree/ <br>\
                    ",
        "reference": "https://www.geeksforgeeks.org/print-nodes-in-top-view-of-binary-tree-set-2/",
    },
    {
        "name": "Serialize and deserialize binary tree",
        "descriptions": "https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/",
        "example": "",
        "reference": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/",
    },
    {
        "name": "Given a string s, find the longest palindromic substring in s",
        "descriptions": "",
        "example": "Input: 'babad'<br>Output: 'bab'<br>Note: 'aba' is also a valid answer.",
        "reference": "https://leetcode.com/problems/longest-palindromic-substring/",
    },
    {
        "name": "Boggle Board Search",
        "descriptions": "Given a dictionary, a method to do lookup in dictionary and \
                        a M x N board where every cell has one character.<br>\
                        Find all possible words that can be formed by a sequence of adjacent characters.<br>\
                        Note that we can move to any of 8 adjacent characters, \
                        but a word should not have multiple instances of same cell.",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/boggle-set-2-using-trie/",
    },
    {
        "name": "Find the shortest path between two vertecise in the weighted graph",
        "descriptions": "Based on dijkstra's algorithm",
        "example": "https://www.youtube.com/watch?v=IG1QioWSXRI",
        "reference": "https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/",
    },
    {
        "name": "Deepcopy of linked list",
        "descriptions": "Given a linked list where each node has two pointers, \
                        one to the next node and one to a random node in the list, \
                        clone the linked list.",
        "example": "https://www.byte-by-byte.com/randomlinkedlist/",
        "reference": "https://www.youtube.com/watch?v=xF9goDxk5nM",
    },
    {
        "name": "Find duplicates in given array",
        "descriptions": "Find duplicates in O(n) time and O(1) extra space \
                        Given an array of n elements which contains elements from 0 to n-1, <br>\
                        with any of these numbers appearing any number of times.<br>\
                        Find these repeating numbers in O(n) and using only constant memory space.",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/",
    },
    {
        "name": "Longest Palindromic Subsequence",
        "descriptions": "Given a sequence, find the length of the longest palindromic subsequence in it",
        "example": "",
        "reference": "https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/",
    },

]


for question in questions:
    q_name = session.query(Questions).filter_by(name=question["name"]).first()
    if not q_name:
        q = Questions(name=question["name"], descriptions=question["descriptions"],
                         example=question["example"], reference=question["reference"])
        session.add(q)
        session.commit()
