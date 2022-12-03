from BinarySearchTreeMap import BinarySearchTreeMap as BST


def restore_bst(prefix_lst): # prefix is C L R
    def restore_helper(prefix_lst, start, end):
        if start > end: # base case
            return None
        
        root = BST.Node(BST.Item(prefix_lst[start])) # current
        i = start + 1 # head of left subtree
        
        while i <= end and prefix_lst[i] < root.item.key: # find the end of the left subtree
            i += 1
        
        root.left = restore_helper(prefix_lst, start + 1, i - 1) # left subtree
        root.right = restore_helper(prefix_lst, i, end) # right subtree -- rest of the list
        return root

    bst = BST()
    bst.root = restore_helper(prefix_lst, 0, len(prefix_lst) - 1)
    return bst


def main():
    prefix_lst = [9,7,3,1,5,13,11,15]
    bst = restore_bst(prefix_lst)
    bst.print_tree()


if __name__ == '__main__':
    main()
