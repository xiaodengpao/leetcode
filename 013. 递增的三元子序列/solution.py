#!python3
import sys

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 遍历一次

        first = sys.maxsize
        second = sys.maxsize

        for num in nums:
            if num < first:
                first = num
            elif num>first and num<second:
                second = num
            elif num > second:
                return True
        
        return False



if __name__ == "__main__":
    ret = Solution().increasingTriplet([0,4,2,1,0,-1,-3])
    print(ret)