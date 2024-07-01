# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head.next or not head: return None #EC
        # slow=fast=head
        # prev=None#need to mainpulate the mid ele, so storing the prev ele is needed !
        # while fast and fast.next:
        #     prev=slow
        #     slow=slow.next
        #     fast=fast.next.next

        # prev.next=slow.next
        # return head

        #M2 - without a 3rd variable 
        if not head or not head.next:return None 
        slow=head
        fast=head.next 
        while fast.next and fast.next.next:
            slow=slow.next 
            fast=fast.next.next 
        slow.next=slow.next.next 
        return head 