class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #better appr ----------
        r=""
        p,q,c=len(a)-1,len(b)-1,0
        
        while(p>=0 or q>=0):
            s=c                      #so that sum gets set to the pre round carry !
            if p>=0:
                s+=ord(a[p])-ord('0')#this will give a num as 1/0
                p-=1
            if q>=0:
                s+=ord(b[q])-ord('0')
                q-=1
                
            c=1 if s>=2 else 0;     #sum 2 /more will occur only when 2->1's or 3->1's
            
            r+=str(s%2)
            
        if c!=0: #to see @ last if we have a carry we have to add it right with out string !
            r+=str(c)
            
        return r[::-1]

        """
        #appr 2 without using ord()------------

            def addBinary(self, a: str, b: str) -> str:
                s = []
                carry = 0
                i = len(a) - 1
                j = len(b) - 1

                while i >= 0 or j >= 0 or carry:
                    if i >= 0:
                        carry += int(a[i])
                        i -= 1
                    if j >= 0:
                        carry += int(b[j])
                        j -= 1
                    s.append(str(carry % 2))
                    carry //= 2

                return ''.join(reversed(s))
        """

        """
        #naive apr --------------
        
        #b="10110"
        def bin_dec(b):
            dec=0
            for i in range(len(b)):
                dec+=int(b[i])*(2**(len(b)-1-i))
            return dec
        #print(bin_dec(b))
        def dec_bin(d):
            b=""
            while(d>0):
                b=b+str(d%2)
                d=d//2
            b=b[::-1]    
            return b if b!="" else "0" #else case to handle "0"+"0" => "0" without this it returns a empty string !
        return dec_bin(bin_dec(a)+bin_dec(b))
        #print(dec_bin(10))"""
        
        