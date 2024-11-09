class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        count = 0
        for i in range(n):
            count+=1
            dp[i][i] = 1
        for idx in range(n-1):
            if s[idx] == s[idx+1]:
                dp[idx][idx+1] = 1
                count+=1
        for length in range(3,n+1):
            for i in range(n-length+1):
                #j-i+1 = length -> j = i+length-1
                j = i+length-1
                # print((i,j))
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    count +=1
        # for d in dp:
        #     print(d)
        return count
