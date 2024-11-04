# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        when is depth 0?
        no root
        '''
        if not root:
            return 0
        
        
        '''
        Length of the tree = going throught the deepest level
        how should i go deepest?
        => Maybe DFS
        '''

        '''
        how do i find know the length?
        1. track each level => queue
        2. pass on the info about the depth => DFS with info
        3. recursion
        '''
        left, right = None, None
        if root.left:
            left = root.left
        if root.right:
            right = root.right

        return max(self.maxDepth(left), self.maxDepth(right)) + 1

        '''
        What is recursion runtime?
        => O(n) since it visits every node
        What is memory size?
        => O(n) max =, O(logn) least since if balanced tree, the depth will be logn
        '''
