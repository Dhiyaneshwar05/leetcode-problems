class Solution:

    def search(self, nums: List[int], target: int) -> int:
        #M2 - revised code 
        #NOTE: ref BS.ipynb for detailed expln
        #1. find sorted and unsorted part 
        #2. chk for value in sored part -> proceed 
        #3. if val in unsorted part -> proceed finding sorted and unsorted part 
        #till u get the ele in the sorted half 
        #4. if val is not present return -1 

             #NOTE: what if the nums is not at all rotated ??
             #TODO: dry run for abv case 

        l,h=0,len(nums)-1
        pos=-1 

        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target: return mid 
            #find sorted nums 
            if nums[l]<=nums[mid]: #if True: 1st half is sorted 
                if nums[l]<=target and target<=nums[mid]:#chk if the target is present in this sorted part 
                    h=mid-1
                else: #not presnt in sorted 1st half 
                    l=mid+1
            
            else:#if True: 2nd half is sorted (only one part can be sorted @ a time)
                if nums[mid]<=target and target<=nums[h]:
                    l=mid+1
                else: 
                    h=mid-1
        return -1 

        #M1 - very naive and bad code- uses BS 3 times -> hell nahhhh 
        #dont recommand this code 

        # def min_bs(nums):
        #     l=0
        #     h=len(nums)-1
        #     m=(l+h)//2
        #     while(l<h):
        #         if nums[m]<nums[h]:
        #             h=m
        #             m=(l+h)//2
        #         else:
        #             l=m+1
        #             m=(l+h)//2
        #     return l

        # t=target 
        # min_index=min_bs(nums)
        
        # if t==nums[min_index]:#found at min_index
        #     return min_index#print("found at m idx")
            
        # elif t in nums[:min_index]:#if target left to min_idx
        #     #print("on left of m idx",nums[:min_index],"min idx--",min_index)
        #     l=0
        #     h=min_index-1
        #     while(l<=h):
        #         m=(l+h)//2
        #         #print("l,m,h--",l,m,h)
        #         if nums[m]==t:
        #             #print("--found @:",m)
        #             return m 
        #         elif nums[m]>t:
        #             h=m
        #         else:
        #             l=m+1
        #     return l
        #     if (l>h):
        #         return -1
        
        # elif t in nums[min_index+1:]:
        #     #print("on right on m idx")
        #     h=len(nums)
        #     l=min_index+1
        #     while(l<=h):
        #         m=(l+h)//2
        #         #print("l,m,h--",l,m,h)
        #         if nums[m]==t:
        #             #print("--found @:",m)
        #             return m 
        #         elif nums[m]>t:
        #             h=m
        #         else:
        #             l=m+1
        #     return l
        # #if right to min_idx
        # else:
        #     print("not present in list--")
        #     return -1
    
