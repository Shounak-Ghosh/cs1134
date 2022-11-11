from DoublyLinkedList import DoublyLinkedList

class MidStack:
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.mid = None
    
    def __len__(self):
        return len(self.dll)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        self.dll.add_first(e)
        if self.mid == None:
            self.mid = self.dll.header.next
        elif len(self) % 2 == 1:
            self.mid = self.mid.prev
        
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.dll.first()
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if len(self) % 2 == 0:
            self.mid = self.mid.next
        return self.dll.delete_first()
    
    def mid_push(self, e):
        if self.is_empty():
            self.push(e)
        else:
            self.dll.add_before(self.mid, e)
            if len(self) % 2 == 0:
                self.mid = self.mid.prev