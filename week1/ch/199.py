# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = dict()
        if root == None:
            return []

        ans[0] = root.val
        def solve(node, level):
            if node == None:
                return
            if node.left == None and node.right == None:
                return

            if level in ans:
                pass
            else:
                if node.right:
                    ans[level] = node.right.val
                else:
                    ans[level] = node.left.val
            
            solve(node.right,level+1)
            solve(node.left,level+1)

        solve(root,1)
        return list(ans.values())
