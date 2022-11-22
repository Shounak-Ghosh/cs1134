from LinkedBinaryTree import LinkedBinaryTree


def min_and_max(bin_tree):
    def minmax_helper(node):
        if not node:
            return
        else:
            l = minmax_helper(node.left)
            r = minmax_helper(node.right)
            if not l:
                l = (node.data, node.data)
            if not r:
                r = (node.data, node.data)
        return (min(node.data, l[0], r[0]), max(node.data, l[1], r[1]))
    
    return minmax_helper(bin_tree.root)


def main():
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

    print(min_and_max(LBT))


if __name__ == "__main__":
    main()
