from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):
    def is_height_balanced_helper(node):
        if not node:
            return 0, True
        elif node.right and not node.left:
            rheight, rbal = is_height_balanced_helper(node.right)
            return 1 + rheight, rbal and rheight <= 1
        elif node.left and not node.right:
            lheight, lbal = is_height_balanced_helper(node.left)
            return 1 + lheight, lbal and lheight <= 1
        else:
            lheight, lbal = is_height_balanced_helper(node.left)
            rheight, rbal = is_height_balanced_helper(node.right)
            return 1 + max(lheight,rheight), abs(lheight - rheight) <= 1 and lbal and rbal

    height, bal = is_height_balanced_helper(bin_tree.root)
    return bal

def main():

    LBT = LinkedBinaryTree()
    LBT.root = LinkedBinaryTree.Node(3)
    LBT.root.left = LinkedBinaryTree.Node(2)
    LBT.root.right = LinkedBinaryTree.Node(7)
    LBT.root.left.left = LinkedBinaryTree.Node(9)
    #LBT.root.left.right = LinkedBinaryTree.Node(1)
    LBT.root.right.left = LinkedBinaryTree.Node(8)
    LBT.root.right.right = LinkedBinaryTree.Node(4)
    LBT.root.right.left.right = LinkedBinaryTree.Node(1)
    LBT.root.right.left.left = LinkedBinaryTree.Node(5)

    LBT.print_tree()

    print(is_height_balanced(LBT))

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

    print(is_height_balanced(LBT))

if __name__ == '__main__':
    main()
