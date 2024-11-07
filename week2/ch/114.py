# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        dummy = TreeNode()
        last = [dummy]
        goto_list = [root]

        while goto_list:
            cur_node = goto_list.pop(-1)
            print("current node:",cur_node.val)
            
            if cur_node.right is not None:
                goto_list.append(cur_node.right)
                print("appending right:",cur_node.right.val)
            if cur_node.left is not None:
                goto_list.append(cur_node.left)
                print("appending left:",cur_node.left.val)
            
            cur_node.left = None
            cur_node.right = None
            last[0].right = cur_node
            last[0] = cur_node

        return last[0].right
