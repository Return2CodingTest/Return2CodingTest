class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        pacific = []
        atlantic = []
        
        rowMax = len(heights)
        colMax = len(heights[0])
    
    
        def dfs(r,c,beforeHeight,visited):
        
            if r<0 or r>=rowMax or c<0 or c>=colMax or (r,c) in visited :
                return
        
            if heights[r][c] < beforeHeight : 
                return
        
            visited.append((r,c))
        
            dfs(r+1,c,heights[r][c],visited)
            dfs(r-1,c,heights[r][c],visited)
            dfs(r,c+1,heights[r][c],visited)
            dfs(r,c-1,heights[r][c],visited)
        
        for r in range(rowMax):
            dfs(r,0,-1,pacific)
            dfs(r,colMax-1,-1,atlantic)
            
        for c in range(colMax):
            dfs(0,c,-1,pacific)
            dfs(rowMax-1,c,-1,atlantic)
    
        return list(set(pacific) & set(atlantic))
