#!python3



# 这样做会超时，DP问题基本可以考虑用二维数组来解决

# class Solution:
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         if m > 1 and n > 1:
#             return (self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1))
        
#         if n == 1 or m == 1:
#             return 1



# 方法二

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0 for i in range(max(m,n))] for j in range(max(m,n))]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


if __name__ == "__main__":
    Solution().uniquePaths(3, 2)
