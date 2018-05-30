#!python3


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}

        # 子串的头 和 尾
        start = 0
        end = 0
        dic[start] = 0
        for index, word in enumerate(s):
            if s[start:end].find(word) == -1:
                end = end + 1
                dic[start] = dic[start] + 1
            
            # 发现重复
            else:
                start = s[start:end].find(word) + start + 1
                dic[start] = index - start + 1
                end = end + 1


        max_val = 0
        for (k,v) in  dic.items():
            if v > max_val:
                max_val = v
        
        return max_val


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abbacade") == 4)
    print(Solution().lengthOfLongestSubstring("pwwkew") == 3)
