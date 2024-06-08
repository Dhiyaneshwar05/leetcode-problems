# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next 
            if fast == slow:
                #set slow to head and from now on take one step 
                slow=head 
                while slow != fast:
                    slow=slow.next
                    fast=fast.next
                return slow 
        return None  
