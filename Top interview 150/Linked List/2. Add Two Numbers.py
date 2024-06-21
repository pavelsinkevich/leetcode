'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        PreviousNode = None
        FirstNode = None
        carry_over = 0
        is_done = False
        while not is_done:
            num1 = 0
            num2 = 0
            try:
                num1 = l1.val
                l1 = l1.next
            except:
                pass
            try:
                num2 = l2.val
                l2 = l2.next
            except:
                pass
            current_number = num1 + num2 + carry_over
            carry_over = current_number // 10
            current_number = current_number % 10
            currentNode = ListNode(current_number, None)
            if PreviousNode:
                PreviousNode.next = currentNode
                if not FirstNode:
                    FirstNode = PreviousNode
            PreviousNode = currentNode
            is_done = l1 is None and l2 is None and carry_over == 0
        if not FirstNode:
            FirstNode = PreviousNode
        return FirstNode
    
l1 = [2,4,3]
l2 = [5,6,4]
for i in reversed(range(len(l1))):
    if i == len(l1) - 1:
        l1[i] = ListNode(l1[i], None)
    else:
        l1[i] = ListNode(l1[i], l1[i+1])
for i in reversed(range(len(l2))):
    if i == len(l2) - 1:
        l2[i] = ListNode(l2[i], None)
    else:
        l2[i] = ListNode(l2[i], l2[i+1])


obj = Solution()
res = obj.addTwoNumbers(l1[0], l2[0])
res1 = []
while res:
    res1.append(res.val)
    res = res.next
print(res1)