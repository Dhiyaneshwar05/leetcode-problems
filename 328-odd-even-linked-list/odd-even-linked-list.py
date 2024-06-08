# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #constraints: solve in single pass O(n), without no extra DS O(1)
        if head is None or head.next is None:return head
        odd_mover=head
        even_mover=head.next 
        even_head=head.next #storing the even_head to later append

        while odd_mover.next and even_mover.next:
            odd_mover.next=odd_mover.next.next
            odd_mover=odd_mover.next

            even_mover.next=even_mover.next.next 
            even_mover=even_mover.next 

        # even_mover.next=None
        odd_mover.next=even_head

        return head 
        