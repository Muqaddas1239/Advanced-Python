# 9. Stack

# Stack is a linear data structure.
# It follows the LIFO principle, LIFO stands for Last In, First Out.
# The element inserted last is removed first.

# Stack Operations

# 1. Push: Push is used to add an element to the top of the Stack.

# 2. Pop: Pop is used to remove the top element from the Stack.

# 3. Peek: Peek is used to view the top element without removing it.

# 4. isEmpty: isEmpty checks whether the Stack is empty or not.

# 5. Size: # Size returns the number of elements in the Stack.

# Stack using Python List

stack = []

# Push operation
# append() adds an element to the top of the Stack.

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Pop operation
# pop() removes the last element from the Stack.

stack.pop()

print(stack)

# Peek operation
# stack[-1] returns the top element without removing it.

print(stack[-1])

# Checking whether Stack is empty

if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

# Finding the size of Stack

print(len(stack))

# Stack Underflow
# Stack Underflow occurs when we try to remove an element from an empty Stack.

stack = []

if not stack:
    print("Stack Underflow")
else:
    stack.pop()

# Stack Overflow
# Stack Overflow occurs when we try to add an element to a full Stack.
# Python List has dynamic size, so normal Python Lists do not have a fixed capacity.

# Stack using Class

class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, value):
        self.stack.append(value)

    # Pop operation
    def pop(self):
        if not self.stack:
            return "Stack Underflow"

        return self.stack.pop()

    # Peek operation
    def peek(self):
        if not self.stack:
            return "Stack is empty"

        return self.stack[-1]

    # Check whether Stack is empty
    def is_empty(self):
        return not self.stack

    # Return the size of Stack
    def size(self):
        return len(self.stack)

# Creating a Stack object

s = Stack()

# Push elements

s.push(10)
s.push(20)
s.push(30)

# Peek

s.peek()

# Pop

s.pop()

# Stack after Pop

s.stack

# Size

s.size()

# Check if Stack is empty

s.is_empty()

