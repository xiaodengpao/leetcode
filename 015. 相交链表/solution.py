#!python3
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def lengthOfList(head):
    length = 0
    if type(head) != ListNode:
        return length
    
    while(head.next != None):
        head = head.next
        length = length + 1
    length = length + 1
    return length

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if type(headA) != ListNode:
            return None
        if type(headB) != ListNode:
            return None
        len = lengthOfList(headA)
        print(len)
       
        return None
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l2 = ListNode(1)
    Solution().getIntersectionNode(l1, l2)