from ArrayStack import ArrayStack


# name the class "Queue" for gradescope
class StackQueue:
    def __init__(self):
        self.front = ArrayStack()  # stack used when enqueueing
        self.back = ArrayStack()  # stack used when dequeueing

    def __len__(self):
        return len(self.front) + len(self.back)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, val):
        if self.is_empty():  # adding our first element
            self.front.push(val)
        elif self.back.is_empty():  # we are "facing forward"
            self.front.push(val)
        else:  # we are "facing backward", need to flip in order to enqueue
            while not self.back.is_empty():
                self.front.push(self.back.pop())
            self.front.push(val)

    def dequeue(self):
        if self.front.is_empty():  # front stack empty, we are "facing backward"
            return self.back.pop()
        else:  # we are "facing forward", need to flip in order to dequeue
            while not self.front.is_empty():
                self.back.push(self.front.pop())
            return self.back.pop()

    def first(self):
        if self.front.is_empty():  # front stack empty, we are "facing backward"
            return self.back.top()
        else:  # we are "facing forward", need to flip in order to get first
            while not self.front.is_empty():
                self.back.push(self.front.pop())
            return self.back.top()
