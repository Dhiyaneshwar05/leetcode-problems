class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # M1 - internal while loop in worst case TC O(N+(N-1)) ex: 1,1,1,0,0 where k=1
        
        # ml=0
        # l,r=0,0
        # zeros=0
        # while (r<=len(nums)-1):
        #     if nums[r]==0:
        #         zeros+=1
            
        #     if zeros>k:
        #         ml=max(r-l,ml)#update max len 
        #         while zeros>k:
        #             if nums[l]==0:
        #                 zeros-=1
        #             l+=1
        #     r+=1
        # return max(r-l,ml)


        # M2 - not using internal while loop (to move the left pointer)
        l,r=0,0
        ml=0
        zeros=0

        while r<len(nums):
            
            if nums[r]==0: zeros+=1    #can alt write this as zeros+= !nums[r]
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k: #only aceepting and calc the ml if the no of zeros is/under k
                ml=max(ml,r-l+1)    
            r+=1
        return ml

                


        