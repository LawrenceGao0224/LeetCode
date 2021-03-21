# 73. Set Matrix Zeroes

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        set_rows = set()
        set_cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_rows.add(i)
                    set_cols.add(j)
        
        while set_rows:
            temp = set_rows.pop()
            for j in range(n):
                matrix[temp][j] = 0
            
        while set_cols:
            temp = set_cols.pop()
            for i in range(m):
                matrix[i][temp] = 0
        
############################################################################################
# 48. Rotate Image
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]         
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        res = [[] for _ in range(n)]
        for j in range(n):
            for i in range(n-1,-1,-1):
                res[j].append(matrix[i][j])
        print(res)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]

#############################################################################################

# 54. Spiral Matrix
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L = 0
        R = len(matrix[0])
        T = 0
        D = len(matrix)
        result = []
        
        while R > L and D > T:
            for i in range(L, R):
                result.append(matrix[T][i])
            T += 1

            for j in range(T, D):
                result.append(matrix[j][R-1])
            R -= 1
            
            if not (L < R and T < D):
                break
                
            for k in range(R-1, L-1, -1):
                result.append(matrix[D-1][k])
            D -= 1
            
            for l in range(D-1, T-1, -1):
                result.append(matrix[l][L])
            L += 1
           
        return result
                    
                