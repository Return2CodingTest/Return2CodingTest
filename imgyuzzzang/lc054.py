class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n, m = len(matrix), len(matrix[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        direction = 0
        now = (0, 0)
        count = m * n
        
        def getNext(i, j):
            nextI, nextJ = i + dy[direction], j + dx[direction]
            if nextI == n or nextJ == m or matrix[nextI][nextJ] == 101:
                newDir = (direction + 1) % 4
                return ((i + dy[newDir], j+dx[newDir]), newDir)
            return ((nextI, nextJ), direction)

        while True:
            i, j = now
            res.append(matrix[i][j])
            matrix[i][j] = 101
            count -= 1
            if count == 0:
                break
            now, direction = getNext(i,j)
            
        return res
        