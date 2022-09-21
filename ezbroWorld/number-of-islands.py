class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        rowLen = len(grid)
        colLen = len(grid[0])
        # visited=[] 으로 하고 if (r,c) in visited 하면 느림
        visited = [[0 for _ in range(colLen)] for _ in range(rowLen)]
        
        def dfs(r,c):
            
            if r<0 or r>=rowLen or c<0 or c>=colLen or visited[r][c]==1 :
                return
            
            if grid[r][c] == '0' :
                return
            
            visited[r][c]=1

            dfs(r-1,c)
            dfs(r+1,c)          
            dfs(r,c+1)    
            dfs(r,c-1)
            
        for r in range(rowLen):
            for c in range(colLen):
                if visited[r][c] == 0 and grid[r][c] == '1' : 
                    dfs(r,c)
                    ans+=1
                    
        return ans
