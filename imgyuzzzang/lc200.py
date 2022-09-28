# 200. Number of Islands

import copy   
from typing import List

def numIslands( grid: List[List[str]]) -> int:
    visited = copy.deepcopy(grid)
    count = 0
    n = len(grid)
    m = len(grid[0])
    
    def checkValidIsland(i,j):
        return  0<=i<n and 0<=j<m and grid[i][j] == "1" and visited[i][j] == "1"
    
    def dfs(i,j):
        visited[i][j] = "0"
        if checkValidIsland(i-1, j):
            dfs(i-1, j)
        if checkValidIsland(i+1, j):
            dfs(i+1, j)
        if checkValidIsland(i, j-1):
            dfs(i, j-1)
        if checkValidIsland(i, j+1):
            dfs(i, j+1)
            

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1" and visited[i][j] == "1":
                dfs(i,j)
                
                count += 1
    
    return count