# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tortoise and hare
        # initalize fast and slow pointers
            # fast = traverse two at a time
            # head / slow = traverse one at a time
            # if both pointers end up at the same node, cycle is true 


        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            # is operator checks if it is located at the same place in mem
            if head is fast: 
                return True
        return False

        