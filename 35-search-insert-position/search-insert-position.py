class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #NOTE : this is same as lb
        #if same ele present-insert @ first index,
        #if not presnt insert @ lowerbound (just higher than)
        l,h=0,len(nums)-1
        pos=len(nums)#hyp index
        while l<=h:
            mid=(l+h)//2
            if nums[mid]>=target: 
                pos=mid 
                h=mid-1
            else:l=mid+1 
        return pos 