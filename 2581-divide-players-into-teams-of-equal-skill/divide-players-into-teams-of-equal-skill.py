class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        #BUT O(3N){M1,M3} is better than O(NlogN){M2}  chk urself with larger vals (use base 2)

        #M3 O(N)sum+ O(N) counter+ O(N)itr 
        # using inbult counter and chking if pairs count is same (if not cant form a pair and return -1) 
        team_skill=sum(skill)//(len(skill)//2)
        chemistry=0
        ctr=Counter(skill)

        for val,count in ctr.items():
            if count != ctr[team_skill-val]:
                return -1 
            chemistry += (count * val * (team_skill-val))

        #as we go over the entire arr (we add the pairs sum twice to remove that we //2 and return !)
        return chemistry //2  


        #----------------------------------------------
        # #M2 - O(NlogN) - sorting and using 2P  
        # skill.sort() 
        # chemistry,team_skill=0,skill[0]+skill[-1]

        # for i in range(len(skill)//2):
        #     if skill[i] + skill[-i-1] == team_skill: 
        #         chemistry+= (skill[i]*skill[-i-1])
        #     else: 
        #         return -1 
        # return chemistry 
        #----------------------------------------------
        # # M1 - using hmap and chk for differnce in d

        # #NOTE [1,1,2,2,3,3] - Edge case (refer blw) 
        # # TC: O(1)len+O(N)sum+O(N)itr+O(N)chk all 0s, SC: O(N) dict 

        # #make a dict of (val,count) @last all vals count in d must be 0 
        # d={} 
        # chemistry=0 
        # team_skill=sum(skill)//(len(skill)//2) 
        # # print(f'team_skill->{team_skill}')

        # for i in range(len(skill)):
        #     target=team_skill-skill[i]
        #     if target in d and d[target]!=0: #if already 0 cant  remove anything from it ! 
        #         chemistry += (target*skill[i])
        #         d[target]-=1
        #     elif skill[i] in d: d[skill[i]]+=1
        #     else: d[skill[i]]=1
        # # print(f'd is-->{d}')

        # #chk if all the vals in dict are 0 
        # check_all_zero= True 
        # for val in d.values(): 
        #     if val != 0: 
        #         check_all_zero = False 
        #         break        
        # # print(check_all_zero)

        # return chemistry if check_all_zero else -1 

        