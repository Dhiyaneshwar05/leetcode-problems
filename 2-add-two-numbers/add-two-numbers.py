# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0 
        l1v,l2v=0,0
        dummyHead=ListNode(-1,None)
        prev=dummyHead
        while l1 or l2:
            if l1:
                l1v=l1.val
                l1=l1.next
            else:l1v=0# NOTE: need this (ref line  24) IT WONT TAKE 0 automatically, IT TAKES THE LAST VALUE !!!
            if l2:
                l2v=l2.val
                l2=l2.next
            else:l2v=0 #NOTE: need this (ref line 24)
            sum=(l1v+l2v+carry)
            digit=sum%10 
            if sum>9: carry=1
            else: carry=0 #without this u think it will automatiaclly take val 0 but, its NOT, it will take the last value
            prev.next=ListNode(digit,None)
            prev=prev.next 
        #to chk if we have only carry left 
        if carry: prev.next=ListNode(1,None)
        return dummyHead.next
            

        
        
        
        
        
        #TL Exceeded !!!
        # ll=ListNode()
        # dummy=ll
        # carry=0
        # #chking thru 2 lls 
        # while (l1 or l2):
        #     if l1:
        #         v1=l1.val
        #     else:
        #         v1=0
        #     if l2:
        #         v2=l2.val
        #     else:
        #         v2=0

        #     #sum digit 
        #     v=v1+v2+carry
        #     carry=v//10
        #     v=v%10
        #     dummy.next=ListNode(v)
            
        #     #ptr - update
        #     dummy=dummy.next 
        #     if l1:
        #         l1.next
        #     else:
        #         l1=None
        #     if l2:
        #         l2.next
        #     else:
        #         l1=None
        # return dummy.next
            
            


        