### Linked List in Python

A simple linked list implementation in python. You can use it for reference if you want.

#### What is a Linked List?

A linked list is a data structure that has dynamic memory.
In strongly typed languages like C you can use them as a substitute for arrays.
The linked list is made up of 0-n nodes.
Each node has a value and pointer that points to the next node.
The node from which we start is called the head.

#### Why use Linked Lists?

We do not need to allocate fixed memory for linked lists.
If we want, we can continue adding nodes to the list until we run out of memory.
This is in contrast to arrays which usually have fixed memory allocated.

#### Common Linked List Functions

Common functions of linked lists include:
- Traversal: To traverse the list. Simply access the next nodes until you reach the last node.
- Insert: Insert an item into the list. You can insert at the end or the head. Here, I inserted at the head.
- Search: Search for a value in the list. You need to traverse the list.
- Delete: Search for the node, then delete it. There are two cases for this function- Delete the head or any other node. To delete the head, all you have to do is point to a null value and set the next node as the new head, preverably in the reverse order. To delete any other node, find the previous node and the next node, then set the next of the previous to the next of the current. Then set the next of the current to null. Null corresponds to None here.

#### Disadvantages

The disadvantages are as follows:
- Searching a linked list requires you to traverse the list node by node. This means you might need a lot of time to find a node.
- Any method that requires traversing the list will be slow. Such as delete, search and even insert, if you choose to add nodes at the end.

#### Overall Impressions

Due to there being the list data structure in python, there is almost no reason to use a linked list. However, the reality is as a programmer you will have to know about various data types and the linked list is a fundamental data type to learn about. Try creating different functions as practice to see what you can do with the data structure. Linked lists are often used in conjunction with other data structures, like queues or hash tables.
