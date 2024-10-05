class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #BF will cause TLE (see how to do that -> how to gen all perm of a string !!!

        #TC: O(N)
        #SC: O(26) ~ O(1)
        # If s1 is longer than s2, it's not possible for s1 to be a permutation of s2
        if len(s1) > len(s2): return False 

        # Initialize frequency dictionaries for s1 and the current window in s2
        d1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        d2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        # Count the frequency of characters in s1
        for i in range(len(s1)):
            d1[s1[i]] += 1
            d2[s2[i]] += 1
        # Count the frequency of characters in the first window of s2

        # Check if the first window itself matches
        if d1 == d2: return True 

        # Sliding window
        l = 0
        h = len(s1)

        while h < len(s2):
            # Add the next character in the window
            d2[s2[h]] += 1
            # Remove the character that is sliding out of the window
            d2[s2[l]] -= 1
            
            # Move the window forward
            l += 1
            h += 1

            # Check if current window matches
            if d1 == d2:
                return True 

        return False


        # #M1 - using sliding win, hashmap 
        # if len(s1)>len(s2): return False 

        # d1 = dict(map(lambda i: (chr(i), 0), range(ord('a'), ord('z') + 1)))
        # d2 = {k:v for k,v in d1.items()}

        # #count the freq of s1 
        # for i in s1: 
        #     if d1[i] not in d1: d1[i]=1
        #     else: d1[i]+=1
        # l=0
        # h=l+len(s1)
        # #cal the 1st window and update 
        # for i in range(l,h):
        #     if d2[s2[i]] not in d2: d2[s2[i]]=1 
        #     else: d2[s2[i]]+=1
        # if d1==d2: return True 

        # d2[s2[l]]=d2[s2[l]]-1
        # if h+1<len(s2): d2[s2[h+1]]=d2[s2[h+1]]+1
        # l+=1
        # h+=1

        # while h<len(s2):
        #     if d2[s2[i]] not in d2: d2[s2[i]]=1 
        #     else: d2[s2[i]]+=1
            
        #     if d1==d2: return True 

        #     d2[s2[l]]=d2[s2[l]]-1
        #     if h+1<len(s2): d2[s2[h+1]]=d2[s2[h+1]]+1
        #     l+=1
        #     h+=1
        # return False 


        


