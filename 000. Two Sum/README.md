# 题目
Question： Given an array of integers, return indices of the two numbers such that they add up to a specific target. 
You may assume that each input would have exactly one solution.

Example: 
Given nums = [2, 7, 11, 15], target = 9, 
Because nums[0] + nums[1] = 2 + 7 = 9, 
return [0, 1].

descript：给定一个数组，和目标值，求数组里两个数的和等于目标值的下标，数组里数不重复。



# 思路
这里面要考虑两个问题：
1、遍历两两匹配
    最简单粗暴的，可以用两个for循环解决问题。但是 N * N 次循环，有冗余。
    考虑这个情况：10块积木，需要两两互插一下。   取第一块，插其他9块，此为一轮。第一轮过后，第一块积木就都插过了，可以扔掉。然后用剩下的9块中的第一块，插其他8块。一轮又一轮，直到插完。
    类似的，可以反向操作，取[2]插[1], 取[3]插[1,2],取[4]插[1,2,3]………


2、hash表加速匹配
匹配一般都要用hash表，简单快捷，key -- value （key == target - value；value == index）
这样只需要 number == key 就可以判定有符合情况出现。


