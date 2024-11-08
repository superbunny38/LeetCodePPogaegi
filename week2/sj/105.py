# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def inorder_recursion(left, right):
            nonlocal root_index

            if left > right:
                return None

            root_val = preorder[root_index]
            root = TreeNode(root_val)
            root_index += 1

            root.left = inorder_recursion(left, val_to_index[root_val] - 1)
            root.right = inorder_recursion(val_to_index[root_val] + 1, right)
            return root
        
        root_index = 0

        val_to_index = defaultdict(int)
        for idx, value in enumerate(inorder):
            val_to_index[value] = idx
        return inorder_recursion(0, len(preorder) - 1)

        '''
        1. for inorder, if we know the root, we know the left and right of inorder too
        2. recursively, we can use the first index of preorder as the root node of
        recursively called inorder
        3. the recursion has to stop at some time.
        we use the left, right pointer to halt recursion when left > right
        => this can be assumed from the subtree for inorder, the index range becomes
        smaller and smaller the recursion deepens
        4. globally set preorder_index and increase every time each recursion is done
        '''

        '''
        TC: O(n)
        SC: O(n) max height
        '''
