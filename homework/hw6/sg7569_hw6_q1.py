from DoublyLinkedList import DoublyLinkedList


class LinkedQueue:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def __len__(self):
        return len(self.dll)

    def is_empty(self):
        return len(self.dll) == 0

    def enqueue(self, e):
        self.dll.add_last(e)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.dll.delete_first()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.dll.header.next.data
