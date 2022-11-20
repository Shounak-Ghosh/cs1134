'''
q1.

preorder: 1, 5, 3, 8, 6, 7, 2, 4
postorder: 8, 6, 3, 5, 4, 2, 7, 1
inorder: 8, 3, 6, 5, 1, 2, 4, 7

q2.
           3
     1          2
         6    4    7
       5

'''
from DoublyLinkedList import DoublyLinkedList


# q3
def insert_sorted(srt_lnk_lst, elem):
    ptr = srt_lnk_lst.header.next
    while ptr is not srt_lnk_lst.trailer and ptr.data < elem:
        ptr = ptr.next

    # adding before ptr here
    prev_node = ptr.prev
    next_node = ptr
    new_node = DoublyLinkedList.Node(elem)

    # set pointers to insert new node
    new_node.prev = prev_node
    new_node.next = next_node

    prev_node.next = new_node
    next_node.prev = new_node

    # update list size
    srt_lnk_lst.size += 1


# q4
def is_sum_balanced(bin_tree):
    tree_sum, tree_balanced = is_subtree_sum_balanced(bin_tree.root)
    return tree_balanced


def is_subtree_sum_balanced(root):
    if not root:
        # returning (curr_sum, is_balanced), remember empty tree is sum-balanced
        return 0, True
    left_sum, left_balanced = is_subtree_sum_balanced(root.left)
    right_sum, right_balanced = is_subtree_sum_balanced(root.right)

    # Current subtree can only be balanced if both its subtrees are balanced
    # and if the current subtree itself is balanced
    is_balanced = left_balanced and right_balanced and (abs(left_sum - right_sum) <= 1)
    curr_sum = left_sum + right_sum + root.data

    return curr_sum, is_balanced


# q5
from ArrayStack import ArrayStack


class DupStack:
    def __init__(self):
        self.s = ArrayStack()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        if self.is_empty():
            # Pushing "tuples" (2 element lists) into stack:
            #   [elem, count]
            self.s.push([e, 1])
        else:
            top_pair = self.s.top()
            # 2-elem list, not a tuple, so we can modify it
            if e == top_pair[0]:
                top_pair[1] += 1
            else:
                self.s.push([e, 1])
        self.n += 1

    def top(self):
        if self.is_empty():
            raise Exception("Empty DupStack")
        else:
            top_elem, top_count = self.s.top()
            return top_elem

    def top_dups_count(self):
        if self.is_empty():
            raise Exception("Empty DupStack")
        else:
            top_elem, top_count = self.s.top()
            return top_count

    def pop(self):
        if self.is_empty():
            raise Exception("Empty DupStack")
        else:
            top_pair = self.s.top()

            # if top_count == 1, remove pair altogether from stack
            if top_pair[1] == 1:
                self.s.pop()
            # if top_count > 1, update top_count of top element
            else:
                top_pair[1] -= 1

            self.n -= 1
            return top_pair[0]


    def pop_dups(self):
        if self.is_empty():
            raise Exception("Empty DupStack")
        else:
            pop_elem, pop_size = self.s.pop()
            self.n -= pop_size
            return pop_elem
