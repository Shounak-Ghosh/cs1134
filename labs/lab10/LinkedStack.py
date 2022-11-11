from DoublyLinkedList import DoublyLinkedList

class LinkedStack:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def __len__(self):
        return len(self.dll)
    
    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.dll.add_first(e)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.dll.first()
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.dll.delete_first()