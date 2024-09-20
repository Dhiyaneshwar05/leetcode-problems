class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:return False
        else: 
            a=[]
            d={'(':')','[':']','{':'}'}
            for i in s: 
                if i in d: #open bc 
                    a.append(i)
                else: #close bc 
                    if not a or d[a.pop()]!=i:#if there is a ele and not the req one false
                        return False
            return len(a)==0 #True if empty, else False  

        # if len(s)%2==1:
        #     return False 
        # else:
            
        #     #pairs 
        #     d={'}':'{',')':'(',']':'['}
            
        #     stk=[]
            
        #     for i in s:
        #         #open - add in stk 
        #         if i in d.values():
        #             stk.append(i)
        #         else:
        #             #means stk is empty when closing comes 
        #             if len(stk)==0:
        #                 return False 
        #             #take top ele in stack and find if it matches pair
        #             elif d[i]==stk.pop():
        #                 pass 
        #             else:
        #                 return False 
        #     #if empty then True, else False --- TstC- "(("
        #     return not(len(stk))    