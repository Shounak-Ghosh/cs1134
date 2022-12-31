from ArrayStack import ArrayStack

# TODO: pop or top doesn't throw an exception for empty MidStack, and/or no error checking
# TODO: pop improperly rebalances the 2 data structures. Should only rebalance if the stack ends up with 2 more elements than the deque, otherwise the balance gets messed up
# TODO: Multiple calls to mid_push doesn't maintain the midstack property. Need to check sizes of stack and deque to decide which one to insert into

class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, item):
        if self.is_empty():
            self.stack.push((item, item))  # tuple of (item, max)
        elif item > self.stack.top()[1]:  # if item is greater than max
            self.stack.push((item, item))
        else:
            self.stack.push((item, self.stack.top()[1]))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack.top()[0]

    def max(self):
        return self.stack.top()[1]
