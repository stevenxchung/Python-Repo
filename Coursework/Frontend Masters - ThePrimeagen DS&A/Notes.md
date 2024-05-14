# The Last Algorithms Course You'll Need

Notes from [The Last Algorithms Course You'll Need](https://frontendmasters.com/courses/algorithms/) from [ThePrimeagen](https://www.youtube.com/c/theprimeagen) to refresh the foundations.

## 1. Introduction

_No notes for this section_.

## 2. Basics

**Big O**: a way to categorize your algorithms time or memory requirements based on input. In general:

- Growth is respect to input
- Constants are dropped
- The **worse case** scenario is typically what we care about

**Array**: a fixed-size continuous memory space. Given an index, insert, update, and delete are O(1) operations

- There are no built-in methods (insert, update, and delete) for primitive arrays

## 3. Search

- **Linear search**: possibly looks through entire list to find a target value
- **Binary search**: similar to linear search but halves the search space on each iteration

## 4. Sort

- **Bubble sort**: a O(n^2) algorithm that moves the largest value up the array and repeats for each element
- **Linked list**: a linked list is a list of objects that reference each other. In general, `insert()` and `delete()` are O(1) operations if there is a reference provided, `get()` is typically an O(n) operation
- **Queue**: a special implementation of a linked list where adding and removing from the front or end of the list is O(1). The most common queues use a FIFO (first-in-first-out) or LIFO (last-in-last-out) but some may be priority based
- **Stack**: similar to a queue but implements a data structure where LIFO (last-in-first-out) is used

## 5. Arrays

Arrays:

- Pros:
  - O(1) access by index
  - Elements stored in contiguous memory locations
- Cons:
  - Fixed size
  - Typically O(n) access for look-ups
  - Typically O(n) insert/delete since elements need to be shifted

Linked lists:

- Pros:
  - Dynamic size
  - O(1) insert/delete if reference provided
  - Memory allocation as needed vs arrays which may have unused space
- Cons:
  - Pointers increases memory overhead
  - Mostly stuck with O(n) access for look-ups
  - Elements are **not** stored in contiguous memory locations

**Ring buffers**: a circular buffer or circular queue, is a data structure that represents a fixed-size collection of elements arranged in a circular manner. Key characteristics include:

- _Fixed size_: a ring buffer has a fixed maximum capacity defined at the time of creation. Once the buffer is full, new insertions overwrite the oldest data in a cyclic manner

- _Circular behavior_: elements are stored in a circular sequence, meaning that after reaching the last position, the next element wraps around to the first position. This allows the buffer to reuse memory locations efficiently

- _Head and tail pointers_: a ring buffer maintains two pointers: a head pointer indicating the location of the next insertion, and a tail pointer indicating the location of the next element to be removed

- _Efficient insertions and removals_: since the buffer is of fixed size, insertions and removals can be performed in constant time O(1), regardless of the number of elements in the buffer. Overwriting the oldest element during insertions is what allows for this efficiency

- _Wraparound handling_: when the head pointer reaches the end of the buffer, it wraps around to the beginning, and similarly, when the tail pointer reaches the end, it wraps around. This ensures the circular behavior

## 6. Recursion

**Recursion**: a programming concept where a function calls itself in order to solve a problem. In other words, a function in a recursive algorithm solves a smaller version of the same problem, and this process continues until a base case is reached, at which point the recursion stops

Since a recursive function may be complex, to simplify we may think of a recursive function in three steps:

1. **Pre-recursion**: actions(s) _before_ calling the function
2. **Recursion**: recursive function is called
3. **Post-recursion**: action(s) _after_ calling the function

## 6. Quick Sort

**Quick sort**:

- A recursive divide-and-conquer algorithm that works by selecting a "pivot" element from the array and partitioning the other elements into two subarrays according to whether they are less than or greater than the pivot
- It has an average runtime of O(n\*log(n)) but can degrade to O(n^2) if pivot choice is consistently poor
- Is faster in practice for small to medium-sized datasets and has lower memory usage

**Merge sort**:

- A divide-and-conquer algorithm that divides the array into two halves, sorts each half separately, and then merges the sorted halves
- It guarantees a worst-case runtime of O(n\*log(n)) but takes more memory for merging subarrays
- Is more consistent in terms of performance and is a good choice when memory usage is not a concern and stability is desired

## 7. Doubly Linked List

**Doubly linked list**: unlike a singly linked list, where each node contains a value and a reference to the next node in the list, a doubly linked list contains references to **both** the next and the previous nodes

Pros:

- Bidirectional traversal
- Efficient insertions and deletions

Cons:

- Increased memory overhead
- Increased complexity

Doubly linked lists are used in various applications, such as building data structures like deques (double-ended queues), implementing undo/redo functionality, and in scenarios where bidirectional traversal is essential.

## 8. Trees

**Tree**: a widely used data structure that resembles a hierarchical structure similar to a real-world tree. It's composed of nodes connected by edges, where each node holds a value and can have zero or more child nodes. The top node of the tree is called the _root_, and nodes with no children are called _leaves_.

Key characteristics of trees in computer science include:

- _Root_: The topmost node of the tree, serving as the starting point for traversal

- _Node_: Each element in the tree that contains a value and can have child nodes

- _Edge_: The connection between nodes that represents a relationship or link between them

- _Parent node_: A node that has one or more child nodes connected to it

- _Child node_: A node that is connected to a parent node via an edge

- _Leaf node_: A node with no child nodes; it's at the end of a branch

- _Depth_: The distance between the root and a particular node; the root has a depth of 0

- _Height_: The length of the longest path from a node to a leaf; the height of the tree is the height of the root node

## 9. Tree Search

There are two primary types of tree search:

**DFS (depth-first-search)**: starts at the root node and explores as far as possible along each branch before backtracking. It explores one branch of the tree as deeply as possible before moving on to other branches. This means it goes deep before going wide.

Pros:

- Memory efficiency: only needs to care about one branch at a time
- Backtracking: backtracking on a path is automatically built-in
- Effective if speed and depth is necessary

Cons:

- May not find the shortest path
- Can get stuck on cyclic graphs
- Can miss nodes as it goes one branch at a time

**BFS (breadth-first-search)**: BFS explores all the neighbor nodes at the current depth before moving on to the nodes at the next depth level. It explores the nodes level by level, moving outwards from the starting node in a breadth-wise manner.

Pros:

- Shortest path guaranteed for unweighted graphs
- Complete space search
- Level-order search

Cons:

- Less memory efficient as nodes need to be stored
- Not suitable for cyclic graphs
- Not as effective if speed and depth is necessary

**BSTs (binary search trees)** use a binary tree data structure in which each node has at most two child nodes, referred to as the left child and the right child. The nodes in a BST are organized in such a way that for each node:

- All nodes in its _left_ subtree have values _less_ than the node's value
- All nodes in its _right_ subtree have values _greater_ than the node's value

BSTs have a property where searching, insertion, and deletion are O(log(n)) operations on average but can degrade to O(n) if the tree is unbalanced. Variants such as **AVL trees** or **Red-Black trees** are designed to maintain a balanced BST and consequently have a worst-case search, insert, and delete runtime of O(log(n)).

## 10. Heap

**Heap**: a specialized tree-based data structure that satisfies the heap property. The heap property dictates the relationship between parent and child nodes, making heaps particularly useful for priority queues and sorting algorithms. Heaps are not the same as binary search trees; they are often implemented as binary trees but have different rules for organizing and accessing data.

There are two common types of heaps:

- Max heap: the value of each parent node is greater than or equal to the values of its child nodes

- Min heap: the value of each parent node is less than or equal to the values of its child nodes

Key characteristics of heaps include:

- _Shape Property_: A heap is typically structured as a complete binary tree, where all levels are filled except possibly the last level, which is filled from left to right

- _Heap Property_: the heap property (max or min) dictates the ordering of nodes. In a max heap, the parent node is always greater than its child nodes; in a min heap, the parent node is always smaller than its child nodes

- _Priority queue_: heaps are often used to implement priority queues, where the element with the highest (or lowest) priority is accessible in constant time

- _Efficient operations_: heaps allow efficient access to the element with the highest (or lowest) priority. Insertion and deletion operations are also relatively efficient, often performed in logarithmic time complexity

- _Sorting_: heap sort is a sorting algorithm that utilizes the properties of heaps to sort elements in place

The runtime for heaps is as follows:

- Insertion: O(log(n))
- Deletion: O(log(n))
- Peek top: O(1)
- Heapify: O(n)
- Heap sort: O(n\*log(n))

**Trie**: a tree-like data structure used to store and retrieve a dynamic set of strings, usually text-based data like words, prefixes, or sequences. It's particularly efficient for tasks involving string manipulation, such as dictionary lookups, autocomplete suggestions, and searching for words with common prefixes.

## 11. Graphs

**Graphs**: are data structures that consists of a set of nodes (also called vertices) and a set of edges that connect pairs of nodes. Graphs are used to model and represent relationships between various entities. They are a fundamental concept in computer science and have a wide range of applications in various fields.

Key components of a graph include:

- _Nodes (vertices)_: nodes are the fundamental units in a graph. Each node represents an entity, and it can hold additional information, such as a label or value

- _Edges_: edges are connections between nodes, representing relationships between them. An edge can be directed (pointing from one node to another) or undirected (bidirectional between two nodes)

- _Weight_: in some graphs, edges can have a weight or cost associated with them. This weight can represent factors like distance, cost, or any other quantitative measure

Graphs can be categorized into different types based on various characteristics:

- Directed vs. undirected graphs: in directed graphs (digraphs), edges have a direction from one node to another. In undirected graphs, edges have no direction and simply connect nodes

- Weighted vs. unweighted graphs: in weighted graphs, edges have a weight associated with them. Unweighted graphs have no weight associated with edges

- Cyclic vs. acyclic graphs: a graph that contains at least one cycle (a path that starts and ends at the same node) is cyclic, while a graph without cycles is acyclic

- Connected vs. disconnected graphs: a connected graph has a path between every pair of nodes, while a disconnected graph has one or more isolated components

**Dijkstra's algorithm**: a widely used algorithm in computer science for finding the shortest path between nodes in a weighted graph, especially when all edge weights are non-negative.

Key details:

- Maintains a set of nodes whose shortest distance from the source node is known and a set of nodes whose shortest distance is yet to be determined
- Iteratively selects the node with the smallest known distance, relaxes its outgoing edges (updates the distance to its neighbors if a shorter path is found), and repeats the process until the destination node is reached or all reachable nodes have been visited
- Using a _priority queue (min-heap)_ to efficiently find the minimum distance node enables a runtime of O((V + E) \* log(V)), where V is the number of nodes and E is the number of edges

## 12. Maps & LRU

**Map**: stores key-value pairs, allowing efficient retrieval of values associated with specific keys. This data structure is also known by other names in different programming languages and contexts, such as _dictionary_, _hash map_, _associative array_, or _hash table_.

Key features of a map include:

- _Key-value pairs_: each element in a map consists of a unique key and an associated value. The key serves as an identifier for the value

- _Fast lookup_: maps provide fast access to values based on their keys. This is achieved through an underlying mechanism that converts keys into memory addresses, allowing direct retrieval of values without the need to search through the entire data structure

- _Uniqueness of keys_: keys are typically required to be unique within a map. If a duplicate key is added, it may overwrite the existing value

- _Dynamic size_: maps can dynamically grow or shrink as key-value pairs are added or removed

- _Insertion and removal_: you can insert new key-value pairs and remove existing pairs from a map

- _Iterating_: maps often support iteration over keys, values, or both

Worst-case runtimes for maps:

- _Insertion_: O(1)
- _Deletion_: O(1)
- _Lookup_: O(1)

**LRU cache**: a data structure used in computer science to store a limited number of items and efficiently manage their eviction (removal) when the cache reaches its capacity. The main idea behind an LRU cache is to prioritize keeping the most recently used items in the cache and evicting the least recently used items when the cache is full.

Key characteristics of an LRU cache include:

- **Limited capacity**: an LRU cache has a fixed maximum capacity, meaning it can only hold a certain number of items at a time

- **Fast access**: items in the cache are organized in a way that allows for fast access and retrieval. This typically involves using a data structure like a hash table or a linked list

- **LRU policy**: when the cache is full and a new item needs to be added, the cache evicts the item that was least recently accessed or used. This ensures that the most frequently accessed items stay in the cache

- **Item insertion and access**: whenever an item is accessed or inserted into the cache, it becomes the most recently used item, and the cache updates its status accordingly

- **Efficiency**: LRU caches are designed to efficiently maintain the most recently used order of items. Various data structures and algorithms can be used to implement this efficiently

## 13. Wrapping Up
