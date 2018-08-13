#!python3

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # 全数组排序，搞成一个map
        dict = {}
        for index in range(len(strs)):
            str = strs[index]
            str_list = sorted(str)
            sorted_str = "".join(str_list)
            if sorted_str in dict:
                dict[sorted_str].append(str)

            else:
                dict[sorted_str] = [str]
        keys = dict.keys()
        list = []
        for key in keys:
            list.append(dict[key])
                
        return list
        
if __name__ == "__main__":
    Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
