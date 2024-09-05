# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or head is None or head.next is None:return head 

        #find tail and len 
        l=1
        tail=head 
        while tail.next:
            l+=1
            tail=tail.next 
        tail.next=head #make ll circular
        k=k%l
        n=l-k
        while n>0:
            n-=1 #no need to chk for node as its circular ll 
            tail=tail.next #stop at last bfor element 
        head=tail.next 
        tail.next=None #now unlink the last node from head 
        
        return head  