'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
    def setNext(self, next):
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
        
head = [3,2,0,-4]
pos = 1
head_obj = []
for i in range(len(head)):
    ln = ListNode(head[i])
    head_obj.append(ln)
    if i > 0:
        head_obj[i-1].setNext(head_obj[i])
    if i == len(head) - 1 and pos != -1:
        head_obj[i].setNext(head_obj[pos])


obj = Solution()
print(obj.hasCycle(head_obj[0]))