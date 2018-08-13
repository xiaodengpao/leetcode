#!python3



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        min_coin_num = [0]  
        for i in range(1, amount + 1):  
            min_coin_num.append(float('inf'))  
            for value in coins:  
                if value <= i and min_coin_num[i - value] + 1 < min_coin_num[i]:  
                    min_coin_num[i] = min_coin_num[i - value] + 1  
        if min_coin_num[len(min_coin_num)-1] == float("inf") :
            return -1
        
        return min_coin_num[len(min_coin_num)-1]
  

if __name__ == "__main__":
    Solution().coinChange([1, 2, 5], 3)
