# import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #refer BS.ipynb -> more expl there 
        low,high=1,max(piles)
        while low<=high:
            mid=(low+high)//2
            time_with_k_speed = self.hours_taken_with_speed_k(piles,k=mid)
            # if time_with_k_speed == h: return mid - even though u are taking same time, try with lesser speed !!!
            if time_with_k_speed <= h: high=mid-1 #taking less time, but gotta find even lesser time, thus decrease speed k
            else: low=mid+1 #taking more time so increse speed k, to finish in lesser time
        return low 

    def hours_taken_with_speed_k(self,piles,k):
        #ceil the time taken (say 7bananas/(k=3) then it takes 3 hrs not 2 hrs)
        # 2options for O(1) math.ceil or manual mtd
        #manual mtd: for a/b get a+b-1//b this will give ceil 
        #ex: 7/3 => 7+3-1//3 ->9//3 =3 
        hours_taken=0 
        for i in piles: 
            # simply hours_taken += math.ceil(i/k)
            if i/k > 1:
                hours_taken += (i+(k-1))//k
            else: hours_taken += 1 # as 3/7 also takes 1 hr 
        # print(k,hours_taken)
        return hours_taken
        