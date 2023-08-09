# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(None)
        tail = dummyHead
        current1 = list1
        current2 = list2

        while current1 is not None and current2 is not None:
            if current1.val < current2.val:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next

            tail = tail.next
        
        if current1 is None:
            tail.next = current2
        
        if current2 is None:
            tail.next = current1
        
        return dummyHead.next

                