# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return []

        n_so_far = [0]
        ans = [0]
        def solve(node):
            if node.left:
                solve(node.left)
            n_so_far[0]+=1

            if n_so_far[0] == k:
                ans[0] = node.val
                return node.val

            if node.right:
                solve(node.right)
                
        solve(root)
        return ans[0]
