class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        loc = {x: i for i, x in enumerate(target)}
        stack = []
        for x in arr: 
            if x in loc: 
                i = bisect_left(stack, loc[x])
                if i < len(stack):
                    stack[i] = loc[x]
                else:
                    stack.append(loc[x])
        return len(target) - len(stack)
