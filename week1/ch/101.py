# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        store = dict()
        
        def solve(root,lvl):
            if root == None:
                return
            left = None if root.left == None else root.left.val
            right = None if root.right == None else root.right.val
            if lvl in store:
                store[lvl] += [left,right]
            else:
                store[lvl] = [left,right]
            # print(f"left:{left} right:{right} lvl:{lvl}")
            solve(root.left,lvl+1)
            solve(root.right,lvl+1)

        

        def symm(store):
            for lvl, vals in store.items():
                if vals[:int(len(vals)//2)][::-1] != vals[int(len(vals)//2):]:
                    # print(vals[:int(len(vals)//2)])
                    return False
            return True
        
        solve(root,0)
        return symm(store)
