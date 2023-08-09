# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create starting node called dummyHead
        # have tail to current dummyHead node
        # keep track of current as we traverse thru the two lists until one of the list pointers reach the end of the list
        # at each iteration of loop
            # compare the values of nodes at list 1 and list 2
            # point tail.next to the smaller node
            # then we advance the respective current pointer 
        
        current1 = list1
        current2 = list2
        dummyHead = ListNode(None)
        tail = dummyHead

        while current1 and current2: 
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



        