# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def equal(tree1,tree2):
            if tree1 == None and tree2 == None:
                return True
            else:
                if tree1 and tree2:
                    if tree1.val == tree2.val:
                        return equal(tree1.left,tree2.left) and equal(tree1.right,tree2.right)
                    else:
                        return False
                else:
                    return False
        
        return equal(p,q)
