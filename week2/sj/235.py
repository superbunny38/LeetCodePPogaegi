# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Using the trait of the BST
        => all the value left of root node is smaller, right is bigger
        '''

        '''
        start from the root
        check the value. 
        if the value is in between, return that node
        '''

        '''
        if the node is actual value between the two, return that node
        '''

        '''
        if both are smaller, go to left subtree
        if both are bigger, go to right subtree
        '''
        if q.val < p.val:
            p, q = q, p

        
        while root:
            if p.val <= root.val <= q.val:
                return root
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)


        '''
        TC: O(N) in worst, O(logn) in best
        SC: O(N) in worst, O(logn) in best
        '''
    


