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
        lenA = lengthOfList(headA)
        lenB = lengthOfList(headB)
        if lenA > lenB :
            while lenA > lenB:
                lenB = lenB + 1
                headA = headA.next

        elif lenA < lenB:
            while lenA < lenB:
                lenA = lenA + 1
                headB = headB.next

        # 从头到尾遍历
        while headA != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

            
       
        return None
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l2 = ListNode(1)
    Solution().getIntersectionNode(l1, l2)