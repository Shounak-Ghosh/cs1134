import os
from BinarySearchTreeMap import BinarySearchTreeMap as BST

def main():
    term_size = os.get_terminal_size()
    bst = BST()

    # create original tree
    bst[9] = None
    bst[7] = None
    bst[13] = None
    bst[3] = None
    bst[11] = None
    bst[15] = None
    bst[1] = None
    bst[5] = None

    bst.print_tree()
    print('=' * term_size.columns)

    # adding elements operations
    bst[6] = None
    bst.print_tree()
    print('=' * term_size.columns)

    bst[12] = None
    bst.print_tree()
    print('=' * term_size.columns)

    bst[4] = None
    bst.print_tree()
    print('=' * term_size.columns)

    bst[14] = None
    bst.print_tree()
    print('=' * term_size.columns)

    # deleting elements operations
    del bst[7]
    bst.print_tree()
    print('=' * term_size.columns)

    del bst[9]
    bst.print_tree()
    print('=' * term_size.columns)

    del bst[13]
    bst.print_tree()
    print('=' * term_size.columns)

    del bst[1]
    bst.print_tree()
    print('=' * term_size.columns)

    del bst[3]
    bst.print_tree()
    print('=' * term_size.columns)


if __name__ == '__main__':
    main()