class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1

        m=(l+h)//2
        while (l<=h):
            if target not in nums:
                return -1
            elif target<=nums[m]:
                h=m-1
                m=(l+h)//2
            else:
                l=m+1
                m=(l+h)//2
        return l
                