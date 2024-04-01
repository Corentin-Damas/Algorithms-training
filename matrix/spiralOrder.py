from typing import List
class Solution:
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            #left to right on top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top+= 1
            
            # top to bottom last column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -=1
            
            if not(left < right and top < bottom):
                break
            
            #bottom left to bottom right
            for i in range(right-1, left -1, -1):
                res.append(matrix[bottom -1][i])
            bottom -= 1
            
            #bottom to top left
            for i in range(bottom -1, top -1, -1):
                res.append(matrix[i][left])
            left +=1
        return res