class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #BF - O(N) refer striver_bs.ipynb locally 
        #O(log N)- use binary search
        
        l,h=0,len(nums)-1 
        lb,ub=len(nums),len(nums)
        #calc lb
        while l<=h:
            mid=(l+h)//2
            if nums[mid]>=target:
                lb=mid
                h=mid-1
            else: l=mid+1

        #calc ub     
        l,h=0,len(nums)-1 
        while l<=h:
            mid=(l+h)//2
            if nums[mid]>target: 
                ub=mid
                h=mid-1
            else: l=mid+1
        
        if lb==len(nums) or nums[lb]!=target: return -1,-1
        return lb,ub-1
        