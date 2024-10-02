class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        #M2 - eff O(N) soln 
        if sum(arr)%k: return False #cant form pairs in the 1st place 
        #find reminder for all x and store in a dict 
        d={} 
        for i in arr:
            reminder=((i%k)+k)%k#to handle -ve vals 
            d[reminder]=d.get(reminder,0)+1
        print(d)

        #now form pairs with all the eles in dict 
        # rem shld b in range (0-> k)
        if d.get(0): #there exists with rem 0
            if d.get(0)%2!=0: return False #but cant form pairs as of odd count 

        for i in range(1, ((k+1)//2) ):
            target=k-i
            # print(i,target,d.get(i),d.get(target))
            if d.get(i)!=d.get(target): return False 

        if k%2==0: #we would have missed to chk the when k==(k/2):
            if d.get(k//2):
                if d.get(k//2)%2 != 0: return False 

        return True 





        # #M1 - O(N*N) 
        # NOTE long appr => worst one -> wont work in case of duplicates 
        # NOTE we cant remove elements from the arr while we are still traversing (indexing)
        # if sum(arr)%k != 0: return False #as u cant form pairs 
        # removed_idxs=[]
        # for i in range(len(arr)):
        #     m=1 
        #     while i not in removed_idxs and (m*k)-arr[i]<=max(arr):
        #         target = (m*k)-arr[i]
        #         #target idx shld not b in removed_idx => coz alredy we have removed that element !
        #         if target in arr and target!=arr[i] and arr.index(target) not in removed_idxs: 
        #             # arr.remove(i)
        #             # arr.remove((m*k)-i)
        #             #cant remove in the current travesing arr ! thats why using another arr 
        #             print(f'idxs to be removed {i}={arr[i]}, --- ,{arr.index(target)}={target}')
        #             removed_idxs.append(i)
        #             removed_idxs.append(arr.index(target))
        #             break 
        #         else: 
        #             m+=1
        # # print(removed_idxs,len(removed_idxs))
        # if len(removed_idxs)==len(arr): return True #as all the pairs are formed (after removed)
        # else: return False 
