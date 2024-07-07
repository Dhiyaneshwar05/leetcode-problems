class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9: 
            digits[-1]+=1
            return digits
        else:
            digits[-1]=0
            # print(digits)
            carry=1
            # digits[-1]=0
            for i in range(len(digits)-2,-1,-1):
                if digits[i]!=9:
                    digits[i]+=carry
                    return digits
                else:
                    digits[i]=0
                    carry=1
            # print(digits,carry,[carry]+digits)
            if carry:return [carry]+digits
            else: return digits
        
            
        