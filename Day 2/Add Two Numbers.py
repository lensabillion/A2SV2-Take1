# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = 0
        cnt1 = 1
        while l1:
            num1 = num1 + (l1.val * cnt1)
            cnt1 *= 10
            l1 = l1.next
        num2 = 0
        cnt2 = 1
        while l2:
            num2 = num2 + (l2.val * cnt2)
            cnt2 *= 10
            l2 = l2.next
        final_num = num1 + num2
        if final_num==0:
            return ListNode(0)
        
        ans = node = ListNode(None)
        while final_num != 0:
            curr = final_num % 10
            node.next = ListNode(curr)
            final_num //= 10
            node = node.next
        return ans.next
            
            
