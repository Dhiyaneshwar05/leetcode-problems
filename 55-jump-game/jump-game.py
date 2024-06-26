class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        #goal to reach last index
        goal=n-1
        for i in range(n-2,-1,-1):
            print(i)
            if nums[i]+i>=goal:
                goal=i
        print("goal",goal)
        return False if goal else True
                

        