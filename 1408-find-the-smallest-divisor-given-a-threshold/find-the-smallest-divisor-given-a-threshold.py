import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #k is the divisor, max k such that k<=threshold
        
        #to handle the single ele case, nums=[5], thres=2,ans is 5/2=> 3 
        if len(nums)==1: return math.ceil(nums[0]/threshold)
        l,h=1,max(nums)
        while l<=h:
            mid=(l+h)//2
            val=self.sum_with_x_as_divisor(nums,x=mid)
            if val<=threshold: #u might b a soln, but let me try even lesser number as divisor to get a val close/equal to threshold
                h=mid-1
            else: #u cant be a soln,as u exceed threshold, so increment the divisor, to reduce the val than the threshold 
                l=mid+1
        return l
        
    def sum_with_x_as_divisor(self,nums,x):
        sum_with_x=0
        for i in nums: 
            sum_with_x += math.ceil(i/x)
        return sum_with_x