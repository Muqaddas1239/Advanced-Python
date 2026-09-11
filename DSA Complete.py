# 9. Queue
# Queue is a data structure that follows the First-In, First-Out (FIFO) principle
# meaning the first element added is the first one to be removed
#  The insert and delete operations are often called enqueue and dequeue

queue = []

# Adding elements to the queue
queue.append('A')
queue.append('B')
queue.append('K')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("Elements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("Queue after removing elements")
print(queue)

# 10. Linked List
# Linked List is a linear data structure where elements, called nodes, are stored in a sequence
#  Each node contains two parts: the data and a reference (or link) to the next node in the sequence

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__=='__main__':

    # Create a linked list
    # 10 -> 20 -> 30
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    
    # Print the list
    temp = head
    while temp != None:
        print(temp.data, end = " ")
        temp = temp.next


# 11. Tree
# Tree Data Structure is a non-linear data structure in which a collection of elements known as nodes are connected to each other via edges 
# such that there exists exactly one path between any two nodes

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None
        
def printInorder(root):
    if(root == None):
        return
    printInorder(root.left)
    print(root.data, end = " ")
    printInorder(root.right)

if __name__ == '__main__':
    
    # Construct Binary Tree of 4 nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    
    printInorder(root)


# 12. Heap
# Heap is a complete binary tree that satisfies the heap property
#  It can be used to implement a priority queue

import heapq
a = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(a)

# printing created heap
print ("The created heap is:", a)

# Push 4 into the heap
heapq.heappush(a, 4)

# printing modified heap
print ("The modified heap after push is:", a)

# using heappop() to pop smallest element
print ("The smallest element is:", heapq.heappop(a))

#13. Graphs
# Graph is a non-linear data structure consisting of a collection of nodes and edges

# Function to add an edge between two vertices
def addEdge(adj, u, v, w):
    adj[u].append((v, w))
    adj[v].append((u, w))

def displayAdjList(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(f"{{{j[0]}, {j[1]}}} ", end="")
        print()

def main():
  
    # Create a graph with 3 vertices and 3 edges
    V = 3
    adj = [[] for _ in range(V)]

    # Now add edges one by one
    addEdge(adj, 1, 0, 4)
    addEdge(adj, 1, 2, 3)
    addEdge(adj, 2, 0, 1)

    print("Adjacency List Representation:")
    displayAdjList(adj)

if __name__ == "__main__":
    main()


# 14. Dynamic Programming
# Dynamic Programming (DP) is a technique for solving problems by breaking them into smaller subproblems 
# and storing their solutions to avoid redundant computations
# It is used when a problem has overlapping subproblems and optimal substructure

  