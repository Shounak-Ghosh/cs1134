from ArrayQueue import ArrayQueue


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if left is not None:
                self.left.parent = self
            self.right = right
            if right is not None:
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def count_nodes(self):
        def subtree_count(root):
            if root is None:
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)

    def sum(self):
        def subtree_sum(root):
            if root is None:
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return left_sum + right_sum + root.data

        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if (root.left is None) and (root.right is None):
                return 0
            elif root.right is None:  # left is not None
                left_height = subtree_height(root.left)
                return 1 + left_height
            elif root.left is None:  # right is not None
                right_height = subtree_height(root.right)
                return 1 + right_height
            else:  # both subtrees are not None
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if self.is_empty():
            raise Exception("Tree is empty")
        return subtree_height(self.root)

    def preorder(self):
        def subtree_preorder(root):
            if root is None:
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)

    def inorder(self):
        def subtree_inorder(root):
            if root is None:
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def postorder(self):
        def subtree_postorder(root):
            if root is None:
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)

    def breadth_first(self):
        if self.is_empty():
            return
        bfs_queue = ArrayQueue()
        bfs_queue.enqueue(self.root)
        while bfs_queue.is_empty() == False:
            curr_node = bfs_queue.dequeue()
            yield curr_node
            if curr_node.left is not None:
                bfs_queue.enqueue(curr_node.left)
            if curr_node.right is not None:
                bfs_queue.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    # question 2 on hw 7
    def leaves_list(self):
        # generates all the leaves of the tree in order
        def leaves_list_helper(node):
            if not node:
                pass
            elif not node.left and not node.right:  # leaf node found
                yield node.data
            else:
                # check left and right subtrees
                yield from leaves_list_helper(node.left)
                yield from leaves_list_helper(node.right)

        # passing the generator in to the list constructor
        return list(leaves_list_helper(self.root))

    # question 4 on hw 7
    # general intuition: O(1) memory - cannot use any other data structures, 
    # but we can use the tree itself
    def iterative_inorder(self):
        curr_node = self.root # initialize pointer to root

        while curr_node:
            if not curr_node.left: # if no left child, yield current and move right
                yield curr_node.data
                curr_node = curr_node.right
            else: # if left child exists, find the rightmost node in the left subtree
                left_node = curr_node.left 
                while left_node.right and left_node.right is not curr_node: # keep moving right
                    left_node = left_node.right
                if not left_node.right: # set the rightmost node's right child to current node
                    left_node.right = curr_node # link created, left_node.right was previously None
                    curr_node = curr_node.left 
                else: # left_node.right is curr_node
                    left_node.right = None  # reset the changes made to the tree
                    yield curr_node.data
                    curr_node = curr_node.right

    # method to print the tree (root is the leftmost value)
    def print_tree(self):
        def subtree_print(root, level):
            if root is None:
                return
            else:
                subtree_print(root.right, level + 1)
                print("    " * level, root.data)
                subtree_print(root.left, level + 1)

        subtree_print(self.root, 0)
        print()


def eval_exp_tree(exp_t):
    def subtree_eval_exp(root):
        if (root.left is None) and (root.right is None):
            return root.data
        else:
            left_arg = subtree_eval_exp(root.left)
            right_arg = subtree_eval_exp(root.right)
            if root.data == "+":
                return left_arg + right_arg
            elif root.data == "-":
                return left_arg - right_arg
            if root.data == "*":
                return left_arg * right_arg
            if root.data == "/":
                return left_arg / right_arg

    return subtree_eval_exp(exp_t.root)
