class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # if the choice is > root(c) then it will excedd the val of c, thus cap high @ root(c)
        high=int(c**0.5)
        d={}
        for i in range(0,high+1):#we need to compare with high too,thus high+1
            val=i**2
            if val not in d:
                d[val]=1
        for i in d:
            if c-i in d:
                return True
        return False

        