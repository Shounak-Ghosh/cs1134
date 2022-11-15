from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.dll = DoublyLinkedList()
        for char in orig_str:
            if self.dll.is_empty():
                self.dll.add_last((char, 1))
            elif self.dll.trailer.prev.data[0] == char:
                self.dll.trailer.prev.data = (
                    char, self.dll.trailer.prev.data[1] + 1)
            else:
                self.dll.add_last((char, 1))

    # TODO: need to reimplement without inbuilt concatenation
    def __add__(self, other):
        # convert self and other to string form and concatenate
        s = self.__repr__()
        o = other.__repr__()
        return CompactString(s + o)
            

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __repr__(self):
        return "".join(char * count for char, count in self.dll)