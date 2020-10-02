"""
DAY 2 NOTES - Lecutre with Beej 9/29



GET(key):
    get the index for the key
    search the linked list at that index for the key
    if found, return the value
    else return None

PUT(key):
    get the index for the key
    search the linked list at that index for the key
    if the key is found, overwrite the value stored there
    else, insert the key and value at the head of the list at that index

    *The idea for every put is, we want to overwrite the value if something is already there, or insert it 

DELETE(key):
    get the index for key
    search the linked list for the key at that index
    if found, delete it, return it
    else, return None
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init(self):
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur

            cur = cur.next
        #If we get here, it's not in the list
        return None

    def delete(self, value):
        if self.head is None:
            return None
        
        if self.head.value == value:
            old_head = self.head

            self.head = self.head.next

            old_head.next = None
            return old_head

    def __str__(self):
        r = ""
        
        cur = self.head
        
        while cur is not None:
            r += f'{cur.value}'
            if cur.next is not None: 
                r += ' -> '
            cur = cur.next
        return r 

ll = LinkedList()

ll.insert_at_head(Node(10))

print(ll)