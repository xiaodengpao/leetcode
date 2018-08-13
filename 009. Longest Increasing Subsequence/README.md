# 题目
给定一个无序的整数数组，找到其中最长上升子序列的长度。


示例 1:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


#思路
dp算法，维护一个一维dp数组，dp[i] 代表 以nums[i]为结尾的最长递增子串（默认值是1，因为可以自递增）
先遍历一次dp[n]，在每一个dp[i]中，继续遍历一遍 0 -> i-1，当nums[i] > nums[j]时，此时可以看做有一个 “以nums[i]为结尾的最长递增子串”
求出 最大长度 dp[i] = max(dp[j]+1, dp[i]) 