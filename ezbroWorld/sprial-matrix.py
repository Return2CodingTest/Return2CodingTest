from collections import deque

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols,dq,checkedNum = len(matrix), len(matrix[0]), deque(), 0
        
        #테두리를 padding
        newBoard = [[0 for _ in range(cols+2)] for _ in range(rows+2)]
        checked = [[True for _ in range(cols+2)] for _ in range(rows+2)]
        
        for i in range(1,rows+1) :
            for j in range(1,cols+1) : 
                checked[i][j] = False
                newBoard[i][j] = matrix[i-1][j-1]
                
        # 1행을 오른쪽부터 담는다.
        for i in range(1,cols+1) : 
            checked[1][i] = True
            checkedNum +=1
            dq.append(newBoard[1][i])
            
        rowP, colP = 1, cols # 다 돌았으면 rowPoint와 colPoint를 각각 1, 3
                            
                
        # checked                               
        ##################################
        #                                #
#  0    #    T     T     T     T     T   #
        #                                #
#  1    #    T     F     F     F     T   #
        #                                #
#  2    #    T     F     F     F     T   #
        #                                #
#  3    #    T     F     F     F     T   #
        #                                # 
#  4    #    T     T     T     T     T   #
        #                                #
        ##################################
        #
        #    0     1     2     3     4
        # newBoard                               
        ##################################
        #                                #
#  0    #    0     0     0     0     0   #
        #                                #
#  1    #    0     1     2   [ 3 ]   0   #
        #                                #
#  2    #    0     4     5     6     0   #
        #                                #
#  3    #    0     7     8     9     0   #
        #                                # 
#  4    #    0     0     0     0     0   #
        #                                #
        ##################################
                
#         def go(mp,flag,rowP,colP) : 
            
#             def moveAndReturnRowCol(mp,flag,rowPoint,colPoint) : 
#                 returnRowCol = [rowPoint + d[mp][0]*flag, colPoint + d[mp][1]*flag]
#                 return returnRowCol
            
#             d=dict()
#             d["col"], d["row"] = [1,0], [0,1]
#             rowP, colP = moveAndReturnRowCol(mp,flag,rowP,colP)
#             while checked[rowP][colP] == False : 
#                 checkedNum += 1
#                 dq.append(newBoard[rowP][colP])
#                 checked[rowP][colP] = True
#                 rowP, colP = moveAndReturnRowCol(mp,flag,rowP,colP)
#             rowP, colP = moveAndReturnRowCol(mp,-flag,rowP,colP)
            
#             return [rowP, colP]
        
        
        while True : 
            if checkedNum >= rows*cols : #다 채워졌으면
                break
                
            # 왼쪽으로 갈 수 있다면
            if checked[rowP][colP-1] == False : 
                colP -= 1
                while checked[rowP][colP] == False : 
                    checkedNum +=1
                    dq.append(newBoard[rowP][colP])
                    checked[rowP][colP] = True
                    colP -= 1
                colP +=1
                
            # 오른쪽으로 갈 수 있다면
            if checked[rowP][colP+1] == False : 
                colP += 1
                while checked[rowP][colP] == False : 
                    checkedNum +=1
                    dq.append(newBoard[rowP][colP])
                    checked[rowP][colP] = True
                    colP += 1
                colP -=1
                
            # 위로 갈 수 있다면
            if checked[rowP-1][colP] == False : 
                rowP -= 1
                while checked[rowP][colP] == False : 
                    checkedNum +=1
                    dq.append(newBoard[rowP][colP])
                    checked[rowP][colP] = True
                    rowP -= 1
                rowP +=1      
                
            # 아래로 갈 수 있다면
            if checked[rowP+1][colP] == False : 
                rowP += 1
                while checked[rowP][colP] == False : 
                    checkedNum +=1
                    dq.append(newBoard[rowP][colP])
                    checked[rowP][colP] = True
                    rowP += 1
                rowP -=1
                
        return list(dq)
