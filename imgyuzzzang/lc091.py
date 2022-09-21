#91. Decode Ways

def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        def checkValidStr(substring):
            return substring[0] != 0 and 0 < int(substring) < 27
 
        
        if checkValidStr(s[0]):
            dp[0] = dp[1] = 1
        else:
            return 0
        
        for i in range(2, n+1):
            if not checkValidStr(s[i-1]):
                dp[i-1] = 0
            if not checkValidStr(s[i-2:i]):
                dp[i-2] = 0

            dp[i] += dp[i-1] + dp[i-2]
            
            if dp[i] == 0:
                return 0
        
        print(dp)
        
        return dp[n]
                