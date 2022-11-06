import ArrayStack

#TODO check if this works
class StackQueue:
    def __init__(self):
        self.front = ArrayStack.ArrayStack()
        self.back = ArrayStack.ArrayStack()

    def enqueue(self, item):
        self.front.push(item)

    def dequeue(self):
        if self.back.is_empty():
            while not self.front.is_empty():
                self.back.push(self.front.pop())
        return self.back.pop()

    def is_empty(self):
        return self.front.is_empty() and self.back.is_empty()

    def size(self):
        return self.front.size() + self.back.size()

    def __str__(self):
        return str(self.front) + str(self.back)
