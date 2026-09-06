# DSA with Python - Data Structures and Algorithms

# 1. List
# List is a built-in dynamic array which can store elements of different data types

a = [10, 20, "ME", 40, True]
print(a)

# 2. Searching Algorithms
#Searching algorithms are used to locate a specific element within a data structure, such as an array, list, or tree

import bisect  
a = [2, 4, 6, 8, 10]

# Linear search using 'in'
print(6 in a)       

# Linear search using 'count'
print(a.count(7) > 0)   

# Binary search using bisect
pos = bisect.bisect_left(a, 8)
print("Found at index:", pos)

# 3. Sorting Algorithms
# Sorting algorithms are used to arrange the elements of a data structure, such as an array, list, or tree, in a particular order
#  typically in ascending or descending order

nums = [5, 3, 8, 1]

# In-place sort
nums.sort()
print(nums)       

# New sorted list (descending)
print(sorted(nums, reverse=True))

# 4. String
# String is a sequence of characters enclosed within single quotes (' ') or double quotes (" ")
# They are immutable, so once a string is created, it cannot be altered

s = "Hello Madam"
print(s)

# 5. Set
# Set is a built-in collection in Python that can store unique elements of different data types
#It is an unordered collection, meaning the elements do not maintain any specific order as they are added
# Sets do not allow duplicate elements and automatically remove duplicates

a = {10, 20, 20, "ALI", "ALI", True, True}
print(a)

# 6. Dictionary
# Dictionary is an mutable, unordered (after Python 3.7, dictionaries are ordered) collection of data 
# that stores data in the form of key-value pair

# Creating a Dictionary
d = {10 : "hello", 20 : "madam", "hello" : "world", 2.0 : 55}
print(d)

# 7. Recursion
# Recursion is a programming technique where a function calls itself in order to solve smaller instances of the same problem
# It is usually used to solve problems that can be broken down into smaller instances of the same problem

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))


# 8. Queue
# Queue is a data structure that follows the First-In, First-Out (FIFO) principle
#  meaning the first element added is the first one to be removed
# The insert and delete operations are often called enqueue and dequeue

queue = []

# Adding elements to the queue
queue.append('A')
queue.append('B')
queue.append('C')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("Elements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("Queue after removing elements")
print(queue)

