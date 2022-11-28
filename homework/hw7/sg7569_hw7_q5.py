from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_expr_str):
    pref_list = prefix_expr_str.split()
    pref_list = [x for x in pref_list if x != ""]  # remove empty strings
    # print(pref_list)

    # takes in the expr list and the current index in the list
    # returns the root of the subtree and the size of the subtree
    def create_expression_tree_helper(pref_list, start_pos):
        # base case
        if start_pos >= len(pref_list):
            return None, 0
        elif pref_list[start_pos] in "+-*/":  # create a node with the operator
            root = LinkedBinaryTree.Node(
                pref_list[start_pos]
            )  # no need for explicit string conversion
            # create left subtree -- will start from the character right after the operator
            left_subtree, left_subtree_size = create_expression_tree_helper(
                pref_list, start_pos + 1
            )
            root.left = left_subtree
            # create right subtree -- will start from the character right after the left subtree
            right_subtree, right_subtree_size = create_expression_tree_helper(
                pref_list, start_pos + left_subtree_size + 1
            )
            root.right = right_subtree
            return root, left_subtree_size + right_subtree_size + 1
        else:  # create a node with the operand
            root = LinkedBinaryTree.Node(int(pref_list[start_pos]))
            return root, 1

    LBT = LinkedBinaryTree()
    LBT.root = create_expression_tree_helper(pref_list, 0)[0]
    return LBT


def prefix_to_postfix(prefix_exp_str):
    pre_exp_tree = create_expression_tree(prefix_exp_str)
    node_list = list(pre_exp_tree.postorder())
    return " ".join([str(node.data) for node in node_list])


def main():
    pref_expr = "* 2 + - 15 6 4"
    expr_tree = create_expression_tree(pref_expr)
    expr_tree.print_tree()
    print(prefix_to_postfix(pref_expr))


if __name__ == "__main__":
    main()
