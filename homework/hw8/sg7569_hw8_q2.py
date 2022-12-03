from BinarySearchTreeMap import BinarySearchTreeMap as BST

def create_chain_bst(n):
    bst = BST()
    for i in range(1,n+1):
        bst.insert(i, None)
    return bst

def create_complete_bst(n):
    def add_items(bst, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        bst.insert(mid, None)
        add_items(bst, start, mid-1)
        add_items(bst, mid+1, end)
        
    bst = BST()
    add_items(bst, 1, n)
    return bst

def main():
    bst = create_chain_bst(10)
    bst.print_tree()

    bst = create_complete_bst(7)
    bst.print_tree()

    bst = create_complete_bst(15)
    bst.print_tree()




if __name__ == '__main__':
    main()