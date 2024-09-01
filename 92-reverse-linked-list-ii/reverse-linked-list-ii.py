# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right: return head 

        dummyHead=ListNode(0)#to handel edge cases 
        dummyHead.next=head 
        prev_left=dummyHead

        #reach prev to left and store it 
        for _ in range(left-1):
            prev_left=prev_left.next 
        # t=0 
        # while t+1==left: 
        #     t+=1
        #     prev_left=prev_left.next 
       
        left_n=prev_left.next  
        prev=None 
        mover=prev_left.next 

        for _ in range(right-left+1):
            next_n=mover.next 
            mover.next=prev 
            prev=mover 
            mover=next_n 
        # while mover is not None:
        #     t+=1
        #     if t==right+1:break
        #     next_n=mover.next 
        #     mover.next=prev 
        #     prev=mover 
        #     mover=next_n
        
        left_n.next=mover  #prev_left.next.next=mover 
        prev_left.next=prev

        return dummyHead.next  


         
