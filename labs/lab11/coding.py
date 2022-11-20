from LinkedBinaryTree import LinkedBinaryTree as lbt
from ArrayStack import ArrayStack as stack


def bt_even_sum(root):
    if not root:
        return 0
    elif root.data % 2 == 0:
        return root.data + bt_even_sum(root.left) + bt_even_sum(root.right)
    else:
        return bt_even_sum(root.left) + bt_even_sum(root.right)

def bt_contains(root,val):
    if not root:
        return False
    elif root.data == val:
        return True
    else:
        return bt_contains(root.left,val) or bt_contains(root.right,val)


def is_full(root):
    if not root:
        return True
    elif root.left and root.right:
        return is_full(root.left) and is_full(root.right)
    elif not root.left and not root.right:
        return True
    else:
        return False

# dfs with stack
def preorder_with_stack(root):
    if not root:
        return

    s = stack()
    s.push(root)

    while not s.is_empty():
        node = s.pop()
        yield(node.data)

        if node.right:
            s.push(node.right)
        if node.left:
            s.push(node.left)

# def merge_bt(root1,root2):
#     # run dfs on both trees
#     dfs1 = [x for x in preorder_with_stack(root1)]
#     dfs2 = [x for x in preorder_with_stack(root2)]

#     # make the lists the same length
#     if len(dfs1) > len(dfs2):
#         dfs2 += [0] * (len(dfs1) - len(dfs2))
#     elif len(dfs2) > len(dfs1):
#         dfs1 += [0] * (len(dfs2) - len(dfs1))
    
#     # sum the lists
#     dfs3 = [x + y for x,y in zip(dfs1,dfs2)]

#     # make a new tree
#     return create_tree_from_preorder(dfs3)

# def merge_bt2(root1,root2):
#     if not root1 and not root2:
#         return
#     elif not root1:
#         return root2
#     elif not root2:
#         return root1
#     else:
#         root1.data += root2.data
#         root1.left = merge_bt2(root1.left,root2.left)
#         root1.right = merge_bt2(root1.right,root2.right)
#         return root1

# def merge_bt3(root1,root2):
#     if not root1 and not root2:
#         return
#     elif not root1:
#         return root2
#     elif not root2:
#         return root1
#     else:
#         root1.data += root2.data
#         root1.left = merge_bt3(root1.left,root2.left)
#         root1.right = merge_bt3(root1.right,root2.right)
#         return root1

# def create_tree_from_preorder(dfs_list):
#     if not dfs_list:
#         return

#     root = lbt.Node(dfs_list[0])
#     s = stack()
#     s.push(root)

#     for i in range(1,len(dfs_list)):
#         node = lbt.Node(dfs_list[i])
#         if dfs_list[i] < s.top().data:
#             s.top().left = node
#             s.push(node)
#         else:
#             while not s.is_empty() and dfs_list[i] > s.top().data:
#                 prev = s.pop()
#             prev.right = node
#             s.push(node)

#     return root

