class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        postfix = [0]*n
        
        for prefix_i in range(n):
            if prefix_i == 0:
                prefix[prefix_i] = nums[0]
            else:
                prefix[prefix_i] = prefix[prefix_i-1]*nums[prefix_i]
        # print("prefix:",prefix)
        for postfix_i in range(n-1,-1,-1):
            if postfix_i == n-1:
                postfix[postfix_i] = nums[-1]
            else:
                postfix[postfix_i] = postfix[postfix_i+1]*nums[postfix_i]
        # print("postfix:",postfix)
        ret = [0]*n
        for i in range(n):
            if i == 0:
                ret[i] = postfix[i+1]
            elif i == n-1:
                ret[i] = prefix[i-1]
            else:
                ret[i] = prefix[i-1]*postfix[i+1]
        return ret 
