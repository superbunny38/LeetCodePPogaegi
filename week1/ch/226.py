# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(treenode):
            if treenode == None:
                return
            tmp = treenode.right
            treenode.right = treenode.left
            treenode.left = tmp
            invert(treenode.left)
            invert(treenode.right)
        
        invert(root)
        return root
