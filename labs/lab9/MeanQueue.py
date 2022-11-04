import ArrayQueue as aq

class MeanQueue:
    def __init__(self):
        self.queue = aq.ArrayQueue()
        self.mean = 0
        self.count = 0

    def __len__(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0
    
    def enqueue(self, item):
        if type(item) == int or type(item) == float:
            self.queue.enqueue(item)
            self.mean = (self.mean * self.count + item) / (self.count + 1)
            self.count += 1
        else:
            raise TypeError("Only integers or floats are allowed")
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.count -= 1
        if self.count == 0:
            self.mean = 0
        else:
            self.mean = (self.mean * (self.count + 1) - self.queue.first()) / self.count
        return self.queue.dequeue()

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.first()
    
    def sum(self):
        return self.mean * self.count

    # def mean(self):
    #     return self.mean

    
    