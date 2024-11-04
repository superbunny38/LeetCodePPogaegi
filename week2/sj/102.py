# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        if no node, return []
        '''
        if not root:
            return []

        '''
        use queue, first put root node into the queue
        while there is a element in root, I do this steps
        
        1. check the length of the queue, and create a 'level' list to put nodes in the level
        2. go through a for loop going 'length' time
        3. process that node and put it in the 'level' list
        4. check left child first, if there is a left child, put it in the back of the queue
        5. check the right child first, if there is a right child, put it in the back of the queue
        '''
        
        q = deque([root])
        result = []
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                cur_node = q.popleft()
                level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            result.append(level)
        return result
