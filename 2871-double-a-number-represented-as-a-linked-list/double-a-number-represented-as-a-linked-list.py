# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val>4: #carry can be either 0 or 1 (so 4*2+1 =9), anyway if>4 then it exceeds 9 (now 10- so double digit)
            head=ListNode(0,head)
        mover=head 
        while mover: 
            mover.val=(mover.val*2)%10
            if mover.next and mover.next.val>4:
                mover.val+=1
            mover=mover.next 
        return head  