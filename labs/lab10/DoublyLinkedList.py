class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        prev_node = node
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        next_node.prev = new_node
        new_node.next = next_node
        self.size += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if(self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)
 
    def delete_last(self):
        if(self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)
    
    # Runtime: O(n), can't do better than this without direct acess to the node
    def __getitem__(self, index):
        if(index >= len(self)):
            raise Exception("Index out of range")
        
        if index < len(self) // 2:
            cursor = self.header.next
            for i in range(index):
                cursor = cursor.next
        else:
            cursor = self.trailer.prev
            for i in range(len(self) - index - 1):
                cursor = cursor.prev
        return cursor.data

    def __iter__(self):
        cursor = self.header.next
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self]) + "]"

    def remove_all(self, elem):
        cursor = self.header.next
        while(cursor.next is not None):
            if(cursor.data == elem):
                next_node = cursor.next
                self.delete_node(cursor)
                cursor = next_node
            else:
                cursor = cursor.next
    
    



