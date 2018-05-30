# 题目
Question： Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


descript：找出最长不重复的连续子串,例如：给定字符串"abcabcbb",那么最长无重复子串是"abc",子串长度为3.给定另一个字符串"bbbb",那么最长无重复子串是"b",子串长度为1.给定字符串"pwwkew",那么最长无重复子串是"wke",子串长度为3.注意必须是原来字符串的子串，"pwke"只是原来字符串的子序列，并非子串。





# 思路
如果是我们要去寻找一个最大子串，要怎么遍历呢？ 比如：b a c a d e

初始化一个空hash，key记录最大子串长度，value记录起始位置

肯定是这样的：从左往右，先找到 a，然后找到 b，然后找到 b,发现和上一个重合。 那么 abb 区域内，最长子串肯定就是ab，再去比较其他的已经没啥意义。
记录hash(2:0)
接下来舍去ab,以b为起始，再找到a，找到c, 找到a,又发现重复,此时baca最大子串是bac。
记录hash(3:2)
舍去bac,以a为起点。 找到d,找到e。
记录hash(5:3)

最终比较一下hash大小