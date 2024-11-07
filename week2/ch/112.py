# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        goto_list = [(root,0)]
        
        while goto_list:
            cur_node, prev_sum = goto_list.pop(0)
            if cur_node.left == None and cur_node.right == None:#leaf node
                if cur_node.val + prev_sum == targetSum:
                    return True
                continue
            if cur_node.left is not None:
                goto_list.append((cur_node.left,cur_node.val+prev_sum))
            if cur_node.right is not None:
                goto_list.append((cur_node.right,cur_node.val+prev_sum))
        return False
