from DoublyLinkedList import DoublyLinkedList
from sg7569_hw6_q1 import LinkedQueue
from sg7569_hw6_q2 import DLLInteger
from sg7569_hw6_q3 import CompactString


def test_dll():
    dll = DoublyLinkedList()
    assert len(dll) == 0

    dll.add_first(1)
    assert len(dll) == 1
    assert dll.header.next.data == 1
    assert dll.trailer.prev.data == 1

    dll.add_first(2)
    assert len(dll) == 2
    assert dll.header.next.data == 2
    assert dll.header.next.next.data == 1

    dll.add_last(3)
    assert len(dll) == 3
    assert dll.trailer.prev.data == 3
    assert dll.trailer.prev.prev.data == 1

    print(dll)


def test_linked_queue():
    pass


def test_integer():
    a = DLLInteger("999")
    print("a", a, a.dll)
    b = DLLInteger("127")
    print("b", b, b.dll)
    c = a + b
    print("a+b", c, c.dll)
    # d = a * b
    # print("a*b", d, d.dll)


def test_compact_string():
    s1 = CompactString("aaaaabbbaaac")
    s2 = CompactString("aaaaaaacccaaaa")
    print(s1, s1.dll)
    print(s2, s2.dll)
    s3 = s1 + s2
    print(s3, s3.dll)
    print(s2 + s1, (s2 + s1).dll)


def main():
    test_dll()
    test_linked_queue()
    test_integer()
    test_compact_string()


if __name__ == "__main__":
    main()
