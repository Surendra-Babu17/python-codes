📘 DSA Codes in Python
🟢 1. Arrays
(a) Reverse an Array
arr = [1, 2, 3, 4, 5]
print(arr[::-1])

(b) Find Maximum and Minimum
arr = [10, 3, 5, 9, 2]
print("Max:", max(arr))
print("Min:", min(arr))

🟡 2. Strings
(a) Check Palindrome
s = "madam"
print(s == s[::-1])

(b) First Non-Repeating Character
s = "aabbcde"
for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:", ch)
        break

🔵 3. Searching
(a) Linear Search
arr = [10, 20, 30, 40]
x = 30
for i in range(len(arr)):
    if arr[i] == x:
        print("Found at index", i)

(b) Binary Search
arr = [10, 20, 30, 40, 50]
x = 30
low, high = 0, len(arr)-1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
        print("Found at index", mid)
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

🔴 4. Sorting
(a) Bubble Sort
arr = [5, 1, 4, 2, 8]
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

(b) Insertion Sort
arr = [5, 2, 9, 1, 5]
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print(arr)

(c) Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]; i+=1
            else:
                arr[k] = R[j]; j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]; i+=1; k+=1
        while j < len(R):
            arr[k] = R[j]; j+=1; k+=1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)

🟣 5. Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

🟠 6. Stack
stack = []
stack.append(10)
stack.append(20)
print(stack.pop())  # 20

🟤 7. Queue
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
print(queue.popleft())  # 10

🔵 8. Recursion
Factorial
def fact(n):
    if n == 0: return 1
    return n * fact(n-1)
print(fact(5))

🔴 9. Trees
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder(root)

🟡 10. Graphs
Adjacency List
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
print(graph)

BFS
from collections import deque
def bfs(graph, start):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(graph[node])

bfs(graph, "A")

DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

dfs(graph, "A")

🟢 11. Dynamic Programming
Fibonacci (DP)
def fib(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print(fib(10))
📘 DSA Codes Continued
🔢 12. Stack (Advanced Operations)
# Stack using List
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

# Pop
print("Popped:", stack.pop())

# Peek
print("Top element:", stack[-1])

# Check Empty
print("Is empty:", len(stack) == 0)

🔢 13. Queue (Advanced)
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)

# Dequeue
print("Dequeued:", queue.popleft())

# Peek
print("Front:", queue[0])

# Check Empty
print("Is empty:", len(queue) == 0)

🔢 14. Sorting Techniques
(a) Selection Sort
arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print("Selection Sort:", arr)

(b) Quick Sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

arr = [10, 7, 8, 9, 1, 5]
print("Quick Sort:", quicksort(arr))

🔢 15. Binary Trees (Traversals)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):   # LNR
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(root):  # NLR
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root): # LRN
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder:", end=" "); inorder(root)
print("\nPreorder:", end=" "); preorder(root)
print("\nPostorder:", end=" "); postorder(root)

🔢 16. Linked List (Advanced)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.display()
ll.delete(20)
print("\nAfter deletion:")
ll.display()

🔢 17. Hashing (Set & Dict)
(a) Using set → Remove duplicates
arr = [1, 2, 2, 3, 4, 4, 5]
unique = set(arr)
print("Unique elements:", unique)

(b) Frequency Count using dict
arr = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print("Frequency:", freq)

🔢 18. Mapping (HashMap / Dictionary Examples)
(a) Student Marks Dictionary
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(students["Bob"])  # Access
students["David"] = 90  # Insert
print(students)

(b) Word Count in a String
sentence = "hello world hello python world"
words = sentence.split()
word_count = {}
for w in words:
    word_count[w] = word_count.get(w, 0) + 1
print("Word Count:", word_count)

(c) Anagram Check using Mapping
s1, s2 = "listen", "silent"
print("Anagram:", sorted(s1) == sorted(s2))
