# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==1: return head 
        
        mover=head 
        dummyHead=ListNode(-1,head)
        prev_part_tail=dummyHead

        while mover:
            kth_node=self.find_kth_node(mover,k)
            if kth_node: 
                next_part_head=kth_node.next 
                kth_node.next=None #unlink the LL 
                curr_part_new_head=self.reverseLL(mover) #rev 
                prev_part_tail.next=curr_part_new_head
                mover.next=next_part_head #link back 
                prev_part_tail=mover    
                mover=next_part_head
            else: #no kth node - remaining as it is link back
                prev_part_tail.next=mover 
                break
        return dummyHead.next 

    def reverseLL(self,node):
        mover=node 
        prev=None
        while mover:
            next_n=mover.next
            mover.next=prev
            prev=mover 
            mover=next_n
        return prev 
    
    def find_kth_node(self,node,k): # if there is a kth node that is returneed, else None is returned 
        mover=node 
        k-=1
        while mover and k>0:
            k-=1
            mover=mover.next 
        return mover 