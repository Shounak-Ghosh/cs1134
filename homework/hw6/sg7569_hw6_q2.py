from DoublyLinkedList import DoublyLinkedList

# name the class "Integer" for gradescope


class DLLInteger:
    def __init__(self, num_str):
        self.dll = DoublyLinkedList()
        for digit in num_str:
            self.dll.add_last(int(digit))

    def __add__(self, other):
        ans = DLLInteger("")
        carry = 0
        # set pointers to the last node in of each list
        a = self.dll.trailer.prev
        b = other.dll.trailer.prev

        # while we have not reached the header node of either list
        while a != self.dll.header and b != other.dll.header:
            sum = a.data + b.data + carry
            carry = sum // 10  # if sum is 10 or more, carry = 1
            ans.dll.add_first(sum % 10)  # add ones digit to ans
            # move pointers to the left one node
            a = a.prev
            b = b.prev

        # if we have reached the end of one list, but not the other
        while a != self.dll.header:
            sum = a.data + carry
            carry = sum // 10
            ans.dll.add_first(sum % 10)
            a = a.prev

        while b != other.dll.header:
            sum = b.data + carry
            carry = sum // 10
            ans.dll.add_first(sum % 10)
            b = b.prev

        # final carry check
        if carry != 0:
            ans.dll.add_first(carry)

        return ans

    # TODO: implement __mul__ method
    def __mul__(self, other):
        pass

    def __repr__(self):
        return "".join(str(d) for d in self.dll)
