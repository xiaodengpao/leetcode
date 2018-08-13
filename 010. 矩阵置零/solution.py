#!python3

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j] == 0):
                    for index in range(rows):
                        if(index != i and matrix[index][j] != 0):
                            matrix[index][j] = "True"

                    for index in range(cols):   
                        if(index != j and matrix[i][index] != 0):
                            matrix[i][index] = "True"
        print(matrix)
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j] == "True"):
                    print(i,j)
                    matrix[i][j] = 0

if __name__ == "__main__":
    Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])
