# 题目
Question： Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.


descript：最长回文子串。就是给定一个字符串S，找出其中的最长回文子串，并返回该子串。


# 思路
暴力枚举法，遍历[0,0], [0,1]. [0,2] ----- [0,n]
在每一个字符串中，遍历S(0,0)   S(0,1),S(1,1)    S(0,2), S(1,2),S(2,2)    S(0,n), S(n-2, n),S(n-1,n)

在判断S(n-1,n) 的时候，有这样一个状态转移方程：

S(0,n) = S(1, n-1) + 2 // if s0 = sn
在判断S(0,n)的时候，就不需要再次进行遍历了，只需要根据转移方程，计算出值。   复杂度O（n*n），比暴力遍历略低 O(n*n*n)



还有一种思路：

字符串S

// if s0 = sn

S(0,n) = S(1, n-1) + 2 

// else :

S(0,n) = MAX{ S(1, n), S(0, n-1) } 


根据此状态方程，可以用一个递归策略，计算出结果
我觉得这个更符合DP的思想
