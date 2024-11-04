# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        how to invert?
        starting from root, switch left and right tree recursively
        should call invertTree to all the node of the childs
        '''

        if not root:
            return None
        
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left
        return root
