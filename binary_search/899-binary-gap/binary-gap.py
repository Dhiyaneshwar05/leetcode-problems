class Solution:
    def binaryGap(self, n: int) -> int:
        #2Pointers, p2 moving pointer, p1 jumping pointer
        #ex- 1000110001 => (4,1,5) => 5
        bin_string=str(bin(n))[2:] 
        p1=0
        p2=1
        max=0
        while p2<len(bin_string):#then only we can limit till last ele
            print("p1,p2: ",p1,p2)
            if bin_string[p2]=="0":
                p2+=1
            else:
                if p2-p1>max:
                    max=p2-p1
                p1=p2
                p2+=1
        return max

        """
        def binaryGap(n):
            #2Pointers, p2 moving pointer, p1 jumping pointer
            #ex- 1000110001 => (4,1,5) => 5
            bin_string=str(bin(n))[2:] 
            print(bin_string,len(bin_string))
            p1=0
            p2=1
            max=0
            while p2<len(bin_string):#then only we can limit till last ele
                print("p1,p2: ",p1,p2)
                if bin_string[p2]=="0":
                    p2+=1
                else:
                    if p2-p1>max:
                        print("--found bigger gap:--max,p2-p1",max,p2-p1)
                        max=p2-p1
                    p1=p2
                    p2+=1
            return max
        print(binaryGap(1121))
        """
                
        