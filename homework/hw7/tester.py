from LinkedBinaryTree import LinkedBinaryTree

def test_iterative_inorder():
    LBT = LinkedBinaryTree()
    LBT.root = LinkedBinaryTree.Node(3)
    LBT.root.left = LinkedBinaryTree.Node(2)
    LBT.root.right = LinkedBinaryTree.Node(7)
    LBT.root.left.left = LinkedBinaryTree.Node(9)
    # LBT.root.left.right = LinkedBinaryTree.Node(1)
    LBT.root.right.left = LinkedBinaryTree.Node(8)
    LBT.root.right.right = LinkedBinaryTree.Node(4)
    LBT.root.left.left.left = LinkedBinaryTree.Node(5)
    LBT.root.left.left.right = LinkedBinaryTree.Node(1)
    LBT.print_tree()

    for item in LBT.iterative_inorder():
        print(item, end=" ")

def main():
    test_iterative_inorder()

if __name__ == '__main__':
    main()