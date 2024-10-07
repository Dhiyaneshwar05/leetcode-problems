class Solution:
    def minLength(self, s: str) -> int:
        #M2 - O(N), O(N)
        #IDEA: insert chars on stk only when its prev is not 'A' / 'C' while having current char as 
        # B or D, atlast cal the len of chars in stk (as that is the final ans)

        stk=[]
        for char in s:
            if stk and ((stk[-1]=='A' and char=='B') or (stk[-1]=='C' and char=='D')):
                stk.pop() #remove the last ele (ie either 'A' or 'C')
                continue 
            else: 
                stk.append(char)
        return len(stk)

        # #M1 - O(N^2), O(N)
        # stk=[] 
        # stk.append(s)
        # while stk: #stk is not empty 
        #     print(stk)
        #     ns=stk.pop()
        #     # print(ns,"\n\n")
        #     l,h=0,1
        #     while h<len(ns):
        #         if ns[l:h+1]=='AB' or ns[l:h+1]=='CD':
        #             stk.append(ns[:l]+ns[h+1:])
        #             # print(f"stk appnd-->{stk},{l},{h},{ns}")
        #             break
        #         l+=1
        #         h+=1
        # return len(ns) #last ele standing's len 
             
                
        