# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            cur = q.popleft()
            if self.isSameTree(cur, subRoot):
                return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return False
    
    '''
    TC: O(MN) because we call isSame for each node in the root, 
    and each will go through M nodes in the subroot

    SC: O(M + N) because max, we will have height of N recursive calls
    and for that last call, in isSame, it can go deep max of M again
    '''
