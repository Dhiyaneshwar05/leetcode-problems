class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # wt_capacity is in range (max(weights),sum(weights))
        # l=min(weights) - as u cant divide a single package, so atleast it should have the max's wt as capacity
        # h=sum(weights) - as in this case u can simply ship all weights in single day, after this also any val > than wont make a diff and simply just take a day

        #edge case for len(wts) == 1 {low=1 and h=0, thus wont enter the loop !!}
        if len(weights)==1: return weights[0] #as it can only be sent as a whole package for that min capacity option in tat weight itself !
        
        l,h=max(weights),sum(weights)
        while l<=h:
            mid=(l+h)//2
            
            if self.can_ship_having_x_capacity(weights, days, x=mid) == 1: #yes u maybe a poss soln, but iam looking for a reduced capacity 
                h=mid-1 
            else: #u cant ship in req days with ur capacity, thus iam increasing ur capacity 
                l=mid+1
            
        return l #polarity hack - refer striver BS on ans  => l going from not possible to possible, h coming from possible to not possible 



    def can_ship_having_x_capacity(self, weights, days, x):
        wt_sum=0
        days_taken=0

        for i in weights:
            wt_sum+=i 
            if wt_sum <= x: #can accomodate
                continue 
            else: #cant accomodate as exceeded 
                days_taken+=1
                wt_sum=i
        if wt_sum: days_taken +=1 #remaing weights (dont worry it wont exceed the capacity, if it would have it will meet the else blk)

        if days_taken<=days: return 1 #possible with this capacity 
        else: return -1 #not possible 
        