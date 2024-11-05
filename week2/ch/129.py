# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = [(root,str(root.val))]
        ans = []
        while queue:
            popped_node, sofarstr = queue.pop(0)
            if popped_node.left:
                queue.append((popped_node.left,sofarstr+str(popped_node.left.val)))
            if popped_node.right:
                queue.append((popped_node.right,sofarstr+str(popped_node.right.val)))
        
            if popped_node.left == None and popped_node.right == None:
                ans.append(int(sofarstr))
        
        return sum(ans)
