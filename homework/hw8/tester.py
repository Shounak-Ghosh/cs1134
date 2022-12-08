from BinarySearchTreeMap import BinarySearchTreeMap as BST
import os

def main():
    term_size = os.get_terminal_size()
    bst = BST()
    bst[7] = None
    bst[5] = None
    bst[1] = None
    bst[14] = None
    bst[10] = None
    bst[3] = None
    bst[9] = None
    bst[13] = None

    bst.print_tree()

    for node in bst:
        print([node, node.left_size], end=' ')
    print()
    print('=' * term_size.columns)

    # try deleting root
    # del bst[7]

    # bst.print_tree()

    # for node in bst:
    #     print([node, node.left_size], end=' ')
    # print()
    # print('=' * term_size.columns)
    

    # try deleting leaf nodes 
    # del bst[3]

    # bst.print_tree()

    # for node in bst:
    #     print([node, node.left_size], end=' ')
    # print()
    # print('=' * term_size.columns)
    # bst[3] = None
    

    # del bst[9]

    # bst.print_tree()

    # for node in bst:
    #     print([node, node.left_size], end=' ')
    # print()
    # print('=' * term_size.columns)
    # bst[9] = None

    # del bst[13]

    # bst.print_tree()

    # for node in bst:
    #     print([node, node.left_size], end=' ')
    # print()
    # print('=' * term_size.columns)
    # bst[13] = None

    # try deleting node with one child
    # del bst[5]

    # bst.print_tree()

    # for node in bst:
    #     print([node, node.left_size], end=' ')
    # print()
    # print('=' * term_size.columns)

    # try deleting node with two children
    # del bst[14]

    # bst.print_tree()

    # for node in bst:
    #     print([node, node.left_size], end=' ')
    # print()
    # print('=' * term_size.columns)

    for i in range(1, bst.n + 1):
        print(bst.get_ith_smallest(i), end=' ')


if __name__ == '__main__':
    main()
