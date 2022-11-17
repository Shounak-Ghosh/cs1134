from DoublyLinkedList import DoublyLinkedList

# similar to a leetcode question: https://leetcode.com/problems/merge-two-sorted-lists/
def merge_linked_lists(lst1, lst2):
    def merge_sublists(n1, n2, dll):
        if n1 == lst1.trailer and n2 == lst2.trailer:
            return dll
        elif n1 == lst1.trailer:
            dll.add_last(n2.data)
            return merge_sublists(n1, n2.next, dll)
        elif n2 == lst2.trailer:
            dll.add_last(n1.data)
            return merge_sublists(n1.next, n2, dll)
        elif n1.data < n2.data:
            dll.add_last(n1.data)
            return merge_sublists(n1.next, n2, dll)
        else:
            dll.add_last(n2.data)
            return merge_sublists(n1, n2.next, dll)

    return merge_sublists(lst1.header.next, lst2.header.next, DoublyLinkedList())


def iterative_merge_linked_lists(lst1, lst2):
    merged_list = DoublyLinkedList()
    l1 = lst1.header.next
    l2 = lst2.header.next

    while l1 != lst1.trailer and l2 != lst2.trailer:
        if l1.data < l2.data:
            merged_list.add_last(l1.data)
            l1 = l1.next
        else:
            merged_list.add_last(l2.data)
            l2 = l2.next

    while l1 != lst1.trailer:
        merged_list.add_last(l1.data)
        l1 = l1.next

    while l2 != lst2.trailer:
        merged_list.add_last(l2.data)
        l2 = l2.next

    return merged_list


def main():
    lst1 = DoublyLinkedList()
    lst1.add_last(1)
    lst1.add_last(3)
    lst1.add_last(5)
    lst1.add_last(6)
    lst1.add_last(8)

    lst2 = DoublyLinkedList()
    lst2.add_last(2)
    lst2.add_last(3)
    lst2.add_last(5)
    lst2.add_last(10)
    lst2.add_last(15)
    lst2.add_last(18)

    merged_list = iterative_merge_linked_lists(lst1, lst2)
    print(merged_list)
    merged_list = merge_linked_lists(lst1, lst2)
    print(merged_list)
    # while merged_list:
    #     print(merged_list.data)
    #     merged_list = merged_list.next


if __name__ == "__main__":
    main()
