from typing import List
class Solution:
    def isValidSudoku(board: List[List[str]]) -> bool:
        # Brut force solution, there is for sure a greedy mode to make it faster especially step 3
                
        for ligne in board:
            tempCount = []
            for n in ligne:
                if n == "." or n == "":
                    continue 
                if n in tempCount:
                    return False     
                tempCount.append(n)
        
        for col in range(9):
            tempCount = []
            for lin in range(9):
                if board[lin][col] == "." or board[lin][col] == "":
                    continue
                if board[lin][col] in tempCount:
                    return False     
                tempCount.append(board[lin][col])
        
        staLin = 0
        staCol = 0
        
        
        for minGrid in range(9):
            tempCount = []
            for x in range(3):
                for y in range(3):
                    n = board[staLin + y][staCol+x]
                    if n == "." or n == "":
                        continue 
                    if n in tempCount:
                        return False     
                    tempCount.append(n)
            staCol += 3
            
            if staCol == 9:
                staLin +=3
                staCol = 0
            if staLin == 9:
                break
            
        
        return True


caseO1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
caseO2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution.isValidSudoku(caseO2))