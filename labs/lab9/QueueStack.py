import ArrayQueue as aq

class QueueStack:
    def __init__(self):
        self._queue = aq.ArrayQueue()
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, item):
        self._queue.enqueue(item)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        self._size -= 1
        for i in range(self._size):
            self._queue.enqueue(self._queue.dequeue())
        return self._queue.dequeue()
    
    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._queue.first()

    # TODO: implement QueueStack with efficient pop and inefficient push

    

