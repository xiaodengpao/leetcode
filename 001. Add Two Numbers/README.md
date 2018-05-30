# 题目
Question： You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example: 
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) 
Output: 7 -> 0 -> 8

descript：有两个链表，它们表示逆序的两个非负数。计算出两个数的和之后，同样逆序输出作为一个链表。需要注意一点：有进位。




# 思路

题目很easy，就是链表进位的问题，进位时要考虑末位进位的情况。

