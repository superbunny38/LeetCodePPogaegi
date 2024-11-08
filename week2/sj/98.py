# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        How do i know that all values of left subtree is smaller than the root val?
        => from the left subtree, which value is max?
        => the most right sided one child of course!!
        '''

        '''
        Same with right subtree.
        The min val of right subtree must be located at the leftmost side child
        '''

        '''
        checking the left subtree condition
        '''
        if root.left:
            left_max = 0
            left_node = root.left
            while left_node.right:
                left_node = left_node.right
            left_max = left_node.val
        
            if root.val <= left_max:
                return False

        '''
        checking the right subtree condition
        '''
        if root.right:
            right_min = 0
            right_node = root.right
            while right_node.left:
                right_node = right_node.left
            right_min = right_node.val

            if root.val >= right_min:
                return False

        '''
        next, return isValidBST for leftsubtree and rightsubtree
        and make sure both return True
        '''
        left_condition = True
        if root.left:
            left_condition = self.isValidBST(root.left)
        
        right_condition = True
        if root.right:
            right_condition = self.isValidBST(root.right)

        return left_condition and right_condition

        '''
        We don't call the recursive function is left or right child is None, 
        so we don't handle this case in the function
        '''

        '''
        TC: O(n) since we visit every node recursively
        SC: O(n) max height can be n
        '''
