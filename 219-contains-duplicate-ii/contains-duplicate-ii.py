class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #M2 - sliding window (window limit is k), within that 2 idnetical nums shld exist !
        #O(N),O(k)
        i=0
        window=set()
        for j in range(len(nums)):
            if j-i > k:
                window.remove(nums[i])
                i+=1
            if nums[j] not in window:
                window.add(nums[j])
            else:
                return True
        return False

        #BF - generate all sub seq and look if there are 2 id vals in them 
        #O(N*N),O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if j-i<=k and nums[i]==nums[j]:
        #             return True
        # return False
        
        