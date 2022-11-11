from DoublyLinkedList import DoublyLinkedList


def reverse_dll_by_data(dll):
    low = dll.header.next  # first node
    high = dll.trailer.prev  # last node

    while low != high:
        low.data, high.data = high.data, low.data
        low = low.next
        if low == high:
            break
        high = high.prev


def reverse_dll_by_node(dll):
    print(dll)
    low = dll.header.next
    high = dll.trailer.prev

    
    while low != high:
        lownext = low.next
        highprev = high.prev

        low.prev.next, high.prev.next = high.prev.next, low.prev.next
        low.next.prev, high.next.prev = high.next.prev, low.next.prev

        low.next, high.next = high.next, low.next
        low.prev, high.prev = high.prev, low.prev

        low = lownext
        if low == high:
            break
        high = highprev





        

        


