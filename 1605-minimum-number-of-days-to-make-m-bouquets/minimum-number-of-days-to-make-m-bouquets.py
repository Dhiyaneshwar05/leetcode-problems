class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        #O(log(max(bD)-min(bD)) * bD) {log N - for BS, N for can_knit_boq..}
        #~O(log N * N)
        #NOTE: refer BS.ipynb for furthur details !

        if m*k > len(bloomDay): return -1 #as we will need more flowers 
        #to find: min days, range(min(bD),max(bD))
        #chk contd: to be k adj  - can_knit_boq_in_x_days
        
        l,h=min(bloomDay),max(bloomDay)
        while l<=h:
            mid=(l+h)//2
            val=self.can_knit_boq_in_x_days(bloomDay,m,k,x=mid)
            if val==1: #possible ans try something with lesser day
                h=mid-1
            else: 
                l=mid+1
        return l

    def can_knit_boq_in_x_days(self,bloomDay,m,k,x):
        flowers_ready=0 #flowers will b ready if it passed the bloomDay
        boqs_made=0 #boqs will b made if it has enuf adj flowers (flowers_ready)
        for i in bloomDay: 
            if i<=x: 
                flowers_ready+=1
            else: 
                boqs_made+=flowers_ready//k
                flowers_ready=0
        boqs_made+=flowers_ready//k #if there is any remaining flowers, with that can a boq be made 
        
        if boqs_made>=m: return 1 #m boqs can be made for the given day 
        else: return -1 



     

        