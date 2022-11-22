from LinkedBinaryTree import LinkedBinaryTree

# TODO finish this implementation
def create_expression_tree(prefix_expr_str):
    pref_list = prefix_expr_str.split()
    pref_list = [x for x in pref_list if x != ""]  # remove empty strings
    print(pref_list)

    # takes in the expr list and the current index in the list
    # returns the root of the subtree and the size of the subtree
    def create_expression_tree_helper(pref_list, start_pos):
        pass

        

    LBT = LinkedBinaryTree()
    LBT.root = create_expression_tree_helper(pref_list, 0)
    LBT.print_tree()
    return LBT

def main():
    pref_expr = "* 2 + - 15 6 4"
    create_expression_tree(pref_expr)

if __name__ == "__main__":
    main()