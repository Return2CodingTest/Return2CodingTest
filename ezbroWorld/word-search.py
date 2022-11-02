
#DFS

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rLen, cLen = len(board), len(board[0])
        checked = set()
    
        def dfs(r, c, n) : 
            if n == len(word) : return True
            if (r<0 or r>= rLen or c<0 or c>=cLen or word[n] != board[r][c] or (r,c) in checked) : 
                return False
            
            checked.add((r,c))
            res = (dfs(r+1, c, n+1) or
            dfs(r-1,c,n+1) or
            dfs(r,c+1,n+1) or
            dfs(r,c-1,n+1))
            checked.remove((r,c))
            
            return res
        
        for r in range(rLen) : 
            for c in range(cLen) : 
                if board[r][c] == word[0] : 
                    if dfs(r,c,0) : return True
        return False
