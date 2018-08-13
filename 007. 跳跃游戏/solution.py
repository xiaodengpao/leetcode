#!python3



class Solution:
    def canJump(self, nums):
        dp = [0 for i in range(len(nums))] # 初始化一个dp一维数组
        ret = True
        for index in range(len(nums)):
            if index == 0:
                dp[index] = nums[index]
            else:
                # 还要判断是否能到达这里
                if dp[index-1] - 1 < 0:
                    # 到这一步，应该直接退出循环了，返回false
                    return False
                else:
                    dp[index] = max(nums[index], dp[index-1] - 1)
                # 选一个最大值
                # maxNum = -1
                # for j in range(index): # 这里的遍历是多余的，只需要比较 i-1 即可
                #     curMax  = dp[j] - (index - j)
                #     if maxNum < curMax:
                #         maxNum = curMax
                # 判断能否到达I点
                # if maxNum >= 0 & maxNum < nums[index]:
                #     maxNum = nums[index]

                # dp[index] = maxNum
        
        if dp[len(nums)-1] < 0:
            return False
        else:
            return True

