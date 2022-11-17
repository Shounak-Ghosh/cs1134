from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.dll = DoublyLinkedList()
        for char in orig_str:
            if self.dll.is_empty():
                self.dll.add_last((char, 1))
            elif self.dll.trailer.prev.data[0] == char:
                self.dll.trailer.prev.data = (char, self.dll.trailer.prev.data[1] + 1)
            else:
                self.dll.add_last((char, 1))

    def __add__(self, other) -> "CompactString":
        # create a new CompactString object
        new_cs = CompactString("")
        # add all characters from self to new_cs
        for char, count in self.dll:
            new_cs.dll.add_last((char, count))

        # check if last character of new_cs is the same as first character of other
        if new_cs.dll.trailer.prev.data[0] == other.dll.header.next.data[0]:
            # if so, combine the counts
            new_cs.dll.trailer.prev.data = (
                new_cs.dll.trailer.prev.data[0],
                new_cs.dll.trailer.prev.data[1] + other.dll.header.next.data[1],
            )
            other.dll.delete_first()

        # add all new characters from other to new_cs
        for char, count in other.dll:
            new_cs.dll.add_last((char, count))

        return new_cs

    def __lt__(self, other):
        s = self.dll.header.next
        o = other.dll.header.next

        while s is not self.dll.trailer and o is not other.dll.trailer:
            if s.data[0] < o.data[0]:  # compare current characters
                return True
            elif s.data[0] > o.data[0]:
                return False
            else:  # if characters are equal, compare counts
                if s.data[1] < o.data[1]:
                    return True
                elif s.data[1] > o.data[1]:
                    return False
                else:  # if counts are equal, move to next character
                    s = s.next
                    o = o.next

        # return True if self is a prexix of other
        if s is self.dll.trailer and o is not other.dll.trailer:
            return True
        else:
            return False

    def __le__(self, other):
        s = self.dll.header.next
        o = other.dll.header.next

        while s is not self.dll.trailer and o is not other.dll.trailer:
            if s.data[0] < o.data[0]:  # compare current characters
                return True
            elif s.data[0] > o.data[0]:
                return False
            else:  # if characters are equal, compare counts
                if s.data[1] < o.data[1]:
                    return True
                elif s.data[1] > o.data[1]:
                    return False
                else:
                    s = s.next
                    o = o.next

        # return True if self is a prexix of other
        if s is self.dll.trailer and o is not other.dll.trailer:
            return True
        # return True if self and other are equal
        elif s is self.dll.trailer and o is other.dll.trailer:
            return True
        else:
            return False

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __repr__(self):
        return "".join(char * count for char, count in self.dll)
