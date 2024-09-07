"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#why is this pblm diff? coz it has a random ptr, its not possible to link it 
#while the node the r ptr points is not even created !
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #M2 - dont store the copied nodes in hm, instead intertwine in org node 
        
        #1. create copy and interwine
        if head is None: return None 
        mover=head 
        while mover: 
            copy_n=Node(mover.val)
            next_n=mover.next 
            mover.next=copy_n
            copy_n.next=next_n
            mover=next_n 

        #2. copy and link the rand ptrs like org_ll
        temp=head 
        while temp: 
            copy_n=temp.next 
            copy_n.random=temp.random.next if temp.random else None
            temp=copy_n.next 
        
        #3. copy next ptrs, and divide ll into org and copy 
        dummyNode=Node(-1)
        res=dummyNode 

        mover=head 
        while mover: 
            copy_n=mover.next
            mover.next=copy_n.next
            res.next=copy_n
            res=res.next
            mover=copy_n.next 
        
        return dummyNode.next #as this is copied LL and org LL will be restored back like normal 

    
        # #M1 - naive soln (makes use of hashmap - extra SC, thus not best soln)
        # if head is None:return None 
        # #create deepcopy with just the data,(no next,rand)
        # d={}
        # mover=head 
        # while mover: 
        #     d[mover]=Node(mover.val) #{org_node:copied_node,,.,.,.,}
        #     mover=mover.next 
        # #estb the links for copied node 
        # temp=head 
        # while temp: 
        #     copynode=d[temp]#as key is org dict and val is copied dict 
        #     copynode.next=d[temp.next] if temp.next else None#without this (=mover.next), it copy also points to org_node.
        #     copynode.random=d[temp.random] if temp.random else None
        #     #the abv chks (1. at last node: d[None],2.when random is None: d[None] -> Not possible  thus we chk !)
        #     temp=temp.next
        # return d[head]