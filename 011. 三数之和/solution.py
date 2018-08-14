#!python3

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # 先对数组进行排序
        
        if len(nums) < 3:
            return []
        # 依次遍历
        for i in range(len(nums)):
            num = nums[i]
            fisrt = num
            
            for j in range(i+1, len(nums)):
                print("j",j)



if __name__ == "__main__":
    Solution().threeSum([-1, 0, 1, 2, -1, -4])
