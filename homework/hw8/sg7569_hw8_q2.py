from BinarySearchTreeMap import BinarySearchTreeMap 
import os

term_size = os.get_terminal_size()

def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for i in range(1, n + 1):
        bst[i] = None
    return bst


def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


def add_items(bst, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    bst[mid] = None
    # bst.print_tree()
    # print('=' * term_size.columns)
    add_items(bst, start, mid - 1)
    add_items(bst, mid + 1, end)


def main():
    bst = create_chain_bst(10)
    bst.print_tree()

    bst = create_complete_bst(7)
    bst.print_tree()

    bst = create_complete_bst(15)
    bst.print_tree()


if __name__ == "__main__":
    main()
