# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        goto_list = [[root]]
        
        while goto_list:
            level_goto_list = []
            level_ans = []
            popped = goto_list.pop(0)
            for goto_ in popped:
                if goto_.left:
                    level_ans.append(goto_.left.val)
                    level_goto_list.append(goto_.left)
                if goto_.right:
                    level_ans.append(goto_.right.val)
                    level_goto_list.append(goto_.right)
            if level_ans:
                ans.append(level_ans)
                goto_list.append(level_goto_list)
        return ans
            
