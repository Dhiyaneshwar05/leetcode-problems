class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #M1 (can use dict, here i use str)
        max_len=-1
        l=""
        
        if len(s)<2: return len(s)
        
        left,right=0,1
        l+=s[left] #adding the 1st ele 
        
        while right<len(s):  
            if s[right] not in l:
                l+=s[right]
                
            else: #right is pres 
                
                if len(l)>max_len:
                    max_len=len(l)
                    
                l="" #flush out l 
                left_pos=s.index(s[right])+1
                l+=s[left_pos]#push that ele to l 
                s=s[left_pos:]
                right=0#right wil get +1 by default 
                
            right+=1
           
        return max(max_len,len(l)) #here again chk max as the last formed string may be the lonmgest EX: "dvdf" 