from typing import List


class Solution:
    def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bot = l, r

                # save the topLeft
                topLeft = matrix[top][l+i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bot -i][l]

                # move bottom right into bottom left
                matrix[bot-i][l] = matrix[bot][r - i]

                # move bottom right into bottom left
                matrix[bot][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft
            r -= 1
            l += 1


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(Solution.rotate(matrix))
