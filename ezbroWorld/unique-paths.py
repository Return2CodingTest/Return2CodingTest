class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m+n-2)/(factorial(m-1) * factorial(n-1)))
    
    def factorial(n: int) -> int:
        result = 1
        for i in range(1, n+1):
            result *=i
            
        return result
