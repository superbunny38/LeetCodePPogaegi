# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        n_depth = 0
        def findDepth(treenode,cur_depth):
            if treenode == None:
                return 0
            return 1+max(findDepth(treenode.left,cur_depth),findDepth(treenode.right,cur_depth))
        return findDepth(root,0)
