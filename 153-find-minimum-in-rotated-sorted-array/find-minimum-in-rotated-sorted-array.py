class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        m=5001 #set to largest val 
        l,h=0,len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]<m: m=nums[mid]
            #find sorted and unsorted parts 
            if nums[l]<=nums[mid]:
                if nums[l]<m: 
                    m=nums[l]
                    l=mid+1
                else: 
                    l=mid+1
            else: #2nd part sorted 
                if nums[mid+1]<=m: 
                    m=nums[mid]
                    h=mid-1
                else: 
                    h=mid-1
        return m


        #M1 - i dont know how i did this DAMNNN !! but it works and seems to be passed !!! 
        # l=0
        # h=len(nums)-1
        # while(l<h):
        #     m=(l+h)//2
        #     if (nums[m]>nums[h]):
        #         l=m+1
        #     else:
        #         h=m
        # return nums[l]