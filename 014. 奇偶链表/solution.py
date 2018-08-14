#!python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if type(head) != ListNode:
            return head
        if head.next == None:
            return head
        
        current_node = head.next
        is_even = True
        last_node  = head
        even_head = None
        even_tail = None
        # 从第二个开始遍历节点
        while current_node != None:
            if is_even:
                if even_head == None:
                    even_head = current_node
                    even_tail = current_node
                else:
                    even_tail.next = current_node
                    even_tail = even_tail.next

                last_node.next = current_node.next
                # 判断
                if current_node.next != None:
                    last_node =  current_node.next

            current_node = current_node.next
            is_even =  not is_even

        last_node.next = even_head
        even_tail.next = None
        return head
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    head = Solution().oddEvenList(l1)
    print(head.val)
    print(head.next.val)
    print(head.next.next.val)
    print(head.next.next.next.val)
