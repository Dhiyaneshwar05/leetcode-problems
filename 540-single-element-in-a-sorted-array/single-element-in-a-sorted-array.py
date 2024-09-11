class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # M2 - BS O(log N)
        #NOTE: always len(nums) will b odd! (2x+1)- make use of that 
        #1. mid is where iam standing now, i want to eliminate either left/right part 
        #2. for that i have to find which part has the unique element 
        #3. For that we use prop: the pairs bfore the unique element will have indexes like even,odd
        #only after the unique element this flow will get disrupted -> so we keep that as chk
        #4. if mid is odd and mid-1'th ele is equal to the mid ele, it follows (even,odd)
        #that means the unique is to the right part (thus eliminate left)
        #5. similarly mid can be even too, for that we chk if mid+1'th ele is same as mid, if so then also 
        #unique is on right part, thus eliminating left 
        #6. every other case; we have to elimiante right (as unique is on left part)
        
        n=len(nums)
        #to trim the s_space, to avoid chks 
        if n==1: return nums[0] #single ele 
        if nums[0]!=nums[1]: return nums[0] #1st ele is unique
        if nums[n-1]!=nums[n-2]: return nums[n-1] #last ele is unique 
        
        l,h=1,n-2 #chked abv and reduced ss now
        while l<=h:
            mid=(l+h)//2
            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]: #mid is the unique ele 
                return nums[mid]
            #ref abv point 1-3 
            elif (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]!=nums[mid-1]): #unique ele in 2nd half 
                l=mid+1
            else: 
                h=mid-1
        return -1 #dummy return statement - but will never b executed


            
            
                

        
        # #M1 bit manipulation - xor 
        # #TC: O(N) SC O(1) 
        # x=1
        # for i in nums:
        #     x^=i
        # return x^1
