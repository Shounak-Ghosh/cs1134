from BinarySearchTreeMap import BinarySearchTreeMap as BST

# worst case: O(h), where h is the height of the bst
def min_max_BST(bst):
    if not bst.root:
        return None
    
    min_key = bst.root
    max_key = bst.root

    while min_key.left:
        min_key = min_key.left
    
    while max_key.right:
        max_key = max_key.right

    return min_key.item.key, max_key.item.key

# find greatest element less than n in tree
def glt_n(bst,n):
    if not bst.root:
        return None

    node = bst.root
    glt = None

    while node:
        if node.item.key <= n:
            glt = node
            node = node.right # go higher
        else:
            node = node.left # go lower

    return glt.item.key if glt else None


def compare_bst(bst1, bst2):
    if not bst1.root and not bst2.root:
        return True

    if not bst1.root or not bst2.root:
        return False

    inlist1 = list(iter(bst1))
    inlist2 = list(iter(bst2))

    return inlist1 == inlist2


def is_bst(root):
    def is_bst_helper(root):
        if not root:
            return True, None, None # bool, min , max

        is_bst_left, min_left, max_left = is_bst_helper(root.left)
        is_bst_right, min_right, max_right = is_bst_helper(root.right)

        if not is_bst_left or not is_bst_right:
            return False, None, None

        if min_right and min_right < root.item.key:
            return False, None, None

        if max_left and max_left > root.item.key:
            return False, None, None

        return True, min_left if min_left else root.item.key, max_right if max_right else root.item.key

    return is_bst_helper(root)[0]

def is_bst_iterative(bst):
    if not bst.root:
        return True

    inlist = list(iter(bst))

    for i in range(len(inlist) - 1):
        if inlist[i] > inlist[i+1]:
            return False

    return True


def lca_bst(bst, n1, n2):
    if not bst.root:
        return None

    node = bst.root

    while node:
        if n1 < node.item.key and n2 < node.item.key: # both elems are less than node key
            node = node.left # move left
        elif n1 > node.item.key and n2 > node.item.key: # both elems are greater than node key
            node = node.right # move right
        else: # one elem is less than node key and one is greater than node key
            return node.item.key

def main():
    # create the example tree
    bst = BST()
    bst[5] = None
    bst[2] = None
    bst[1] = None
    bst[3] = None
    bst[12] = None
    bst[9] = None
    bst[21] = None
    bst[19] = None
    bst[25] = None

    bst.print_tree()

    print(min_max_BST(bst))
    print(glt_n(bst, 21))
    print(glt_n(bst, 4))

    bst2 = BST()
    bst2[1] = None
    bst2[3] = None
    bst2[25] = None
    bst2[5] = None
    bst2[2] = None
    bst2[12] = None
    bst2[9] = None
    bst2[21] = None
    bst2[19] = None
   
    bst2.print_tree()

    print(compare_bst(bst, bst2))
    




if __name__ == "__main__":
    main()






