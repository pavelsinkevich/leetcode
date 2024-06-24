'''Given the head of a linked list, return the list after sorting it in ascending order.'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nodeList = []
        currentNode = head
        while currentNode:
            nodeList.append(currentNode)
            currentNode = currentNode.next
        nodeList.sort(key=lambda x: x.val)
        for i in range(len(nodeList) - 1):
            nodeList[i].next = nodeList[i+1]
        nodeList[-1].next = None
        return nodeList[0]
    
head = [4,2,1,3]
dummyHead = ListNode()
prevNode = dummyHead
for val in head:
    n = ListNode(val)
    prevNode.next = n
    prevNode = n
obj = Solution()
newHead = obj.sortList(dummyHead.next)
res = []
while newHead:
    res.append(newHead.val)
    newHead = newHead.next
print(res)


