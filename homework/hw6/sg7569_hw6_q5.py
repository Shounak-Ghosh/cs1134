from DoublyLinkedList import DoublyLinkedList
# similar to a leetcode question: https://leetcode.com/problems/merge-two-sorted-lists/

def merge_linked_lists(lst1, lst2):
    def merge_sublists(l1, l2):
        if l1 == lst1.trailer:
            return l2
        elif l2 == lst2.trailer:
            return l1
        elif l1.data < l2.data:
            l1.next = merge_sublists(l1.next, l2)
            l1.next.prev = l1
            l1.prev = lst1.header
            return l1
        else:
            l2.next = merge_sublists(l1, l2.next)
            l2.next.prev = l2
            l2.prev = lst1.header
            return l2

    head = merge_sublists(lst1.header.next, lst2.header.next)
    ans = DoublyLinkedList()
    
    while head and head.next:
        ans.add_last(head.data)
        head = head.next
    
    return ans


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
