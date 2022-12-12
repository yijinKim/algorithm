class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        row_start = 0
        row_end = m-1
        col_start = 0
        col_end = n-1
        
        result = []
        
        while row_start<=row_end and col_start<=col_end:
            
            for i in range(col_start, col_end+1):
                result.append(matrix[row_start][i])
            row_start += 1
            if row_start > row_end:
                break
            
            for j in range(row_start, row_end+1):
                result.append(matrix[j][col_end])
            col_end -= 1
            if col_start > col_end:
                break
            
            for i in range(col_end, col_start-1, -1):
                result.append(matrix[row_end][i])
            row_end -= 1
            if row_start > row_end:
                break
                
            for j in range(row_end, row_start-1, -1):
                result.append(matrix[j][col_start])
            col_start += 1
            if col_start > col_end:
                break
        
        return result