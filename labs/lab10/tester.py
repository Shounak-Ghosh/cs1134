from DoublyLinkedList import DoublyLinkedList
from MidStack import MidStack
from LinkedStack import LinkedStack
import reverse_dll

def test_reverse_dll():
    dll = DoublyLinkedList()
    dll.add_last(1)
    dll.add_last(2)
    dll.add_last(3)
    dll.add_last(4)
    # dll.add_last(5)
    print(dll)
    reversedll.reverse_dll_by_data(dll)
    print(dll)

    reversedll.reverse_dll_by_node(dll)
    print(dll)

def test_linked_stack():
    ls = LinkedStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.push(4)

    print(ls.dll)

    ls.pop()
    
    print(ls.dll)

    ls.pop()

    print(ls.dll)

def test_mid_stack():
    ms = MidStack()
    ms.push(1)
    ms.push(2)
    ms.push(3)
    ms.push(4)

    print(ms.dll)

    ms.mid_push(5)
    
    print(ms.dll)

    ms.mid_push(6)

    print(ms.dll)


def test_dll_get_item():
    dll = DoublyLinkedList()
    dll.add_last(1)
    dll.add_last(2)
    dll.add_last(3)
    dll.add_last(4)
    assert dll[0] == 1
    assert dll[1] == 2
    assert dll[2] == 3
    assert dll[3] == 4

    for i in range(4):
        print(dll[i])

def main():
    test_linked_stack()
    print()
    test_mid_stack()
    print()
    test_dll_get_item()
    print()
    test_reverse_dll()

if __name__ == "__main__":
    main()