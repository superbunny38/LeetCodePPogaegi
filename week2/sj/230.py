# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        BST Property
        => value is increasing in inorder traversal
        '''

        '''
        I need to go over inorder traversal and find the kth node
        '''

        '''
        make a counter global variable
        '''
        count = 0

        '''
        make a recursion function for inorder traversal
        '''
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            count += 1
            if count == k:
                return root.val
            root = root.right
        
        '''
        TC: O(N)
        SC: O(N)
        '''
            
