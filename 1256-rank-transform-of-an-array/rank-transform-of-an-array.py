class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # M2 - using hmap and len 
        ranked_d={} 
        for a in sorted(arr): 
            if a in ranked_d:
                continue 
            ranked_d[a]=len(ranked_d)+1
        return list(map(lambda a:ranked_d[a], arr))
        
        
        #M1 - using set() and len 
        # O(N log N) + O(N*N)- to find the index pos 
        # narr=arr[:] #make a copy 
        # narr.sort()

        # ans=[]
        # rank=[]

        # # rank(ele)=> len(set(narr[:ele]))+1
        # for i in arr:
        #     pos=narr.index(i)
        #     ans.append(len(set(narr[:pos]))+1)
        # return ans 
        
            
        