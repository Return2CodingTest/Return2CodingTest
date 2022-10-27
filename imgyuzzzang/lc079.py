class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_col = len(board[0])
        n_row = len(board)
        
        dc = [1, 0, 0, -1]
        dr = [0, 1, -1, 0]
        
        def find(prev, now, word_idx):
            if word_idx >= len(word):
                return True
            nexts = []
            row, col = now
            prev_row, prev_col = prev
            for i in range(4):
                next_row, next_col = row + dr[i], col + dc[i]
                print(prev, (next_row, next_col) )
                if next_row < n_row and next_col < n_col and (next_row, next_col) != prev and board[next_row][next_col] == word[word_idx]:
                    nexts.append((next_row, next_col))
                    if word_idx == len(word) - 1:
                        return True
            if len(nexts) == 0:
                return False
            for _next in nexts: 
                if find(now, _next, word_idx+1):
                    return True
            return False
        
        res = False
        for row in range(n_row):
            for col in range(n_col):
                if board[row][col] == word[0] and find((-1, -1), (row, col), 1):
                    return True
        return False
        
                    