class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #naive apr 
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
            return b if b!="" else "0"
        return dec_bin(bin_dec(a)+bin_dec(b))
        #print(dec_bin(10))
        
        