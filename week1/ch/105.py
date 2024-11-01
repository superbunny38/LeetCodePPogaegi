# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_index_in_preorder = [0]
        
        def solve(inorder):
            
            if len(inorder) == 1:
                ret = TreeNode(val=preorder[root_index_in_preorder[0]])
                # print("built root w/o leaf:",ret.val)
                root_index_in_preorder[0] += 1
                return ret
            if len(inorder) == 0:
                return None
                
            root = TreeNode(val = preorder[root_index_in_preorder[0]])
            # print("\nbuilt root:",preorder[root_index_in_preorder[0]])
            # print("inorder:",inorder)
            root_index = inorder.index(preorder[root_index_in_preorder[0]])
            # print("root index:",root_index)
            root_index_in_preorder[0] += 1
            inorder_left, inorder_right = inorder[:root_index],inorder[root_index+1:]
                
            root.left = solve(inorder_left)
            root.right = solve(inorder_right)
            return root
    
        return solve(inorder)
