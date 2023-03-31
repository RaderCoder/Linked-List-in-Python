class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = Node(head)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def find_value(self,value):
        temp = self.head
        found = False
        while temp:
            if temp.value == value:
                found = True
                break
            else:
                temp = temp.next
        
        return found

    def __repr__(self):
        repstr = ""
        temp = self.head
        
        while temp:
            repstr = repstr + str(temp.value) + " "
            temp = temp.next

        return repstr