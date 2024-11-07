# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        result = []
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur:
                result.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                result.append('#')
        return ' '.join(result)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        
        nodes = data.split()
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1
        while q:
            cur = q.popleft()
            if index < len(nodes) and nodes[index] != '#':
                cur.left = TreeNode(int(nodes[index]))
                q.append(cur.left)
            index += 1
            if index < len(nodes) and nodes[index] != '#':
                cur.right = TreeNode(int(nodes[index]))
                q.append(cur.right)
            index += 1
        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
