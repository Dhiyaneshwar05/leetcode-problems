# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # less usage for API call means => less time call that func instead of N times !
        #BS pblm 
        l,h=1,n
        while l<=h:
            mid=(l+h)//2
            if isBadVersion(mid) == True: #this is a bad but let me chk prev versiond for bad 
                h=mid-1 
            else: #not bad lets chk for some higer version 
                l=mid+1
        return l #opposite polarity, l starts with not bad and ends up in bad, h starts in bad and ends up in bad 
        