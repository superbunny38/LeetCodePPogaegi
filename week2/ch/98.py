# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root,low = -float('inf'),high = float('inf')):
            if root == None:
                return True
            if root.val<=low or root.val>=high:
                return False
            else:
                return solve(root.left,low,root.val) and solve(root.right,root.val,high)
        return solve(root)
