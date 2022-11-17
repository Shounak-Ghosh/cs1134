from DoublyLinkedList import DoublyLinkedList

# name the class "Integer" for gradescope
class Integer:
    def __init__(self, num_str):
        self.dll = DoublyLinkedList()
        for digit in num_str:
            self.dll.add_last(int(digit))

    def __add__(self, other):
        ans = Integer("")
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

    def __mul__(self, other):
        ans = Integer("0")
        carry = 0
        # set pointers to the last node in of each list
        a = self.dll.trailer.prev
        b = other.dll.trailer.prev
        level_count = 0

        while b != other.dll.header:
            level = Integer("")
            while a != self.dll.header:
                product = a.data * b.data + carry
                carry = product // 10
                level.dll.add_first(product % 10)
                a = a.prev
            if carry != 0:
                level.dll.add_first(carry)

            carry = 0
            a = self.dll.trailer.prev
            b = b.prev
            for i in range(level_count):
                level.dll.add_last(0)
            level_count += 1
            ans = ans + level
        return ans

    def __repr__(self):
        # lstrip() removes any leading zeros
        s = "".join(str(d) for d in self.dll).lstrip("0")
        return s if s else "0"