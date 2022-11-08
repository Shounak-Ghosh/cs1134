from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

# TODO do this question
# general idea: stack adjacent to deque


class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def __len__(self):
        return len(self.stack) + len(self.deque)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        # base case
        if self.stack.is_empty():
            self.stack.push(val)
        else:  # general case
            if len(self.stack) == len(self.deque):
                self.stack.push(self.deque.dequeue_first())
            self.deque.enqueue_last(val)

    def pop(self):
        # print("stack: ", self.stack, "deque: ", self.deque)
        popped = self.deque.dequeue_last()
        if not self.stack.is_empty() and self.deque.is_empty():
            self.deque.enqueue_last(self.stack.pop())
        
        return popped

    def top(self):
        if self.deque.is_empty():
            return self.stack.top()
        else:
            return self.deque.last()

    def mid_push(self, val):
        self.stack.push(val)

        
