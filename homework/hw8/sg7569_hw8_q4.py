from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
    # for each node, return the current min difference and the current max node  in the subtree
    def find_min_abs_difference_helper(node):
        if not node: # base case -- return larg min_diff, and 0 for max val
            return float('inf'), 0
        
        l_min_diff, l_max = find_min_abs_difference_helper(node.left)
        r_min_diff, r_max = find_min_abs_difference_helper(node.right)

        min_diff = min(l_min_diff, r_min_diff, abs(node.item.key - l_max), abs(node.item.key - r_max))
        max_val = max(node.item.key, l_max, r_max)

        return min_diff, max_val

    return find_min_abs_difference_helper(bst.root)[0]

def main():
    bst = BinarySearchTreeMap()
    # insert in level-order in order to get the right bst
    bst[9] = None
    bst[7] = None
    bst[20] = None
    bst[4] = None
    bst[17] = None
    bst[25] = None
    bst[1] = None
    bst[6] = None
    
    
    bst.print_tree()

    print(find_min_abs_difference(bst))

if __name__ == '__main__':
    main()
