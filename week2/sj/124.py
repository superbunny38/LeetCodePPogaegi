# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float('inf')

        # post order traversal of subtree rooted at 'node'
        def gainFromSubtree(node):
            nonlocal maxPath
            if not node:
                return 0
            
            # add the gain from the left subtree.
            # if the gain is negative, we can ignore it, or count as 0
            gainFromLeft = max(gainFromSubtree(node.left), 0)
            gainFromRight = max(gainFromSubtree(node.right), 0)

            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)
            return max(gainFromLeft + node.val, gainFromRight + node.val)
        
        gainFromSubtree(root)
        return maxPath
