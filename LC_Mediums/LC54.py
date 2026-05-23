class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        spiral = []
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1

        while True:
            if left > right or up > down: break
            for i in range(left, right + 1): #Go right
                spiral.append(matrix[up][i])
            up += 1
            if left > right or up > down: break
                
            for j in range(up, down + 1): #Go down
                spiral.append(matrix[j][right])
            right -= 1
            if left > right or up > down: break

            for i in range(right, left - 1, -1): # Go left
                spiral.append(matrix[down][i])
            down -= 1
            if left > right or up > down: break

            for j in range(down, up - 1, -1): #Go up
                spiral.append(matrix[j][left])
            left += 1
            if left > right or up > down: break
            
        return spiral


