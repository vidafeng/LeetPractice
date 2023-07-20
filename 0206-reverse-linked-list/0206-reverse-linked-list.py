# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize current pointer to head
        current = head
        # Initialize prev pointer to None/Null
        prev = None
        
        # Run a loop till current points to Null/none
        while current is not None:
            # Hold next in a temp variable
            next = current.next
            # Assign the prev pointer to current's next pointer 
            current.next = prev
            # Assign current to prev, next to current
            prev = current
            current = next
        # Return the prev pointer to get reversed list 
        return prev
        