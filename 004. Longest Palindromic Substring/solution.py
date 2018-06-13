#!python3


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        """
        k = len(s) # 计算字符串的长度
        matrix = [[0 for i in range(k)] for i in range(k)] # 初始化n*n的列表 
        logestSubStr = "" # 存储最长回文子串 
        logestLen = 0 # 最长回文子串的长度 

        for j in range(0, k):
            for i in range(0, j+1): # i可以等于j，所以j+1
                if j - i <= 1: 
                    if s[i] == s[j]: 
                        matrix[i][j] = 1   # 此时f(i,j)置为true 
                        if logestLen < j - i + 1: # 将s[i:j]的长度与当前的回文子串的最长长度相比 
                            logestSubStr = s[i:j+1] # 取当前的最长回文子串 
                            logestLen = j - i + 1 # 当前最长回文子串的长度 
                else:
                    if s[i] == s[j] and matrix[i+1][j-1]: # 判断子串S（i+1, j-1）是否为回文 
                        matrix[i][j] = 1 # 动态规划，记录S（i,j）是回文串
                        if logestLen < j - i + 1: 
                            logestSubStr = s[i:j+1] 
                            logestLen = j - i + 1
        return logestSubStr 

if __name__ == "__main__":
    print(Solution().longestPalindrome("abbaabbasdadawe"))
