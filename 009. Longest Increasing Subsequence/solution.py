#!python3

# 最大自上升序列长度，题目理解错了
# class Solution(object):
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dp = [0 for i in range(len(nums))] # 初始化一个dp一维数组
#         for index in range(len(nums)): # 遍历N
#             if index == 0:
#                 dp[0] = 1
#                 continue
            
#             # 判断 nums[index] > nums[index-1]
#             if nums[index] < nums[index-1]:
#                 dp[index] = dp[index-1]
#                 continue
            
#             # 截取数组，进一步判断
#             maxLen = 1
#             length = index+1
#             for i in range(index):
#                 if nums[length-i-1] > nums[length-i]:
#                     break
#                 maxLen += 1
            
#             if maxLen >= dp[index-1]:
#                 dp[index] = maxLen
#             else:
#                 dp[index] = dp[index-1]
#         print(dp)

#         return dp[len(nums)-1]



# 最大自上升序列长度
class Solution(object):
    def lengthOfLIS(self, nums):
        # 先判断为空
        if(len(nums) == 0):
            return 0
        
        dp = [1 for i in range(len(nums))] # 初始化一个dp一维数组
        for i in range(len(nums)): # 遍历N
            if i == 0:
                dp[0] = 1
                continue
            # 继续从 0 -> i 遍历，找出dp[j]
            for j in range(i):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

if __name__ == "__main__":
    print(Solution().lengthOfLIS([4,10,4,3,8,9]))
