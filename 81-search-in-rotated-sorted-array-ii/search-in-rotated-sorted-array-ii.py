class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #why search in rot sort nums -I wont work 
        #Ex case [3,1,2,3,3,3,3,3], x=3, l=0(3), m=3(3), h=7(3)
        #as by our chk both will be sorted nums and code fails !
        #NOTE here they asked to say True/False not to return the indexes(duplicates) as for that linear search is the only way !

        l,h=0,len(nums)-1
        present=False 

        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target: return True 
            
            #only contd where our prev code fails - coz of duplicates refer abv 
            if nums[l]==nums[mid] and nums[mid]==nums[h]:
                l=l+1
                h=h-1
                continue 
            #as its obv not the target element also,we tend to TRIM THE SEARCH SPACE
            #by removing the element from 1st and last, there may exist even more such vals 
            #so to chk and trim all of the we use "continue"

            #1st part sorted 
            if nums[l]<=nums[mid]:
                if nums[l]<=target and target<=nums[mid]:#presnt in sorted part - first half 
                    h=mid-1
                else: 
                    l=mid+1
            
            #2nd part sorted 
            else: 
                if nums[mid]<=target and target<=nums[h]:#present in sorted part - second half
                    l=mid+1
                else: 
                    h=mid-1 
        return False #ele not present after full trav 





        