class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #M2 sliding window but clearer version
        l,r,ml=0,0,0
        ss=""
        
        while r<len(s):
            if s[r] not in ss:
                ss+=s[r]
                r+=1
            else:#if s[r] in ss
                ml=max(r-l,ml)#curr_ss_len=r-l
                ss="" #reset ss
                l+=1
                r=l
        return max(ml,r-l)


        # #M1 (can use dict, here i use str)
        # max_len=-1
        # l=""
        
        # if len(s)<2: return len(s)
        
        # left,right=0,1
        # l+=s[left] #adding the 1st ele 
        
        # while right<len(s):  
        #     if s[right] not in l:
        #         l+=s[right]
                
        #     else: #right is pres 
        #         if len(l)>max_len:
        #             max_len=len(l)
                    
        #         l="" #flush out l 
        #         left_pos=s.index(s[right])+1
        #         l+=s[left_pos]#push that ele to l 
        #         s=s[left_pos:]
        #         right=0 
        #     right+=1
           
        # return max(max_len,len(l)) #here again chk max as the last formed string may be the lonmgest EX: "dvdf" 