# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        is_l = self.lowestCommonAncestor(root.left,p,q)
        is_r = self.lowestCommonAncestor(root.right,p,q)

        if is_l and is_r:
            return root
        if is_l:
            return is_l
        if is_r:
            return is_r
        if is_l is None and is_r is None:
            return None
