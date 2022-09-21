class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0':
            return 0
        
        # n번째 자리에서 가질 수 있는 조합의 수
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(s)+1):
            if s[i-1] != '0':
                dp[i] +=dp[i-1]
                
            if int(s[i-2] + s[i-1]) >= 0 and int(s[i-2]+s[i-1])<=26:
                dp[i] +=dp[i-2]
                
                
        return dp[len(s)]
