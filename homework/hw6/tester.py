from DoublyLinkedList import DoublyLinkedList

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


def main():
    test_dll()


if __name__ == "__main__":
    main()