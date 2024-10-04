class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        #BUT O(3N) is better than O(NlogN)  chk urself with larger vals (use base 2)

        #TC: O(1)len+O(N)sum+O(N)itr+O(N)chk all 0s, SC: O(N) dict 
        #make a dict of (val,count) @last all vals count in d must be 0 
        d={} 
        chemistry=0 
        team_skill=sum(skill)//(len(skill)//2) 
        # print(f'team_skill->{team_skill}')

        for i in range(len(skill)):
            target=team_skill-skill[i]
            if target in d and d[target]!=0: #if already 0 cant  remove anything from it ! 
                chemistry += (target*skill[i])
                d[target]-=1
            elif skill[i] in d: d[skill[i]]+=1
            else: d[skill[i]]=1
        # print(f'd is-->{d}')

        #chk if all the vals in dict are 0 
        check_all_zero= True 
        for val in d.values(): 
            if val != 0: 
                check_all_zero = False 
                break        
        # print(check_all_zero)

        return chemistry if check_all_zero else -1 

        