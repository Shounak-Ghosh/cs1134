from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()

    def is_empty(self):
        return self.stack.is_empty()
    
    def __len__(self):
        return len(self.stack)
    
    def push(self, item):
        if self.is_empty(): 
            self.stack.push((item,item)) # tuple of (item, max)
        elif item > self.stack.top()[1]: # if item is greater than max
            self.stack.push((item,item))
        else:
            self.stack.push((item, self.stack.top()[1]))
    
    def pop(self):
        return self.stack.pop()[0]
    
    def top(self):
        return self.stack.top()[0]
    
    def max(self):
        return self.stack.top()[1]

    
