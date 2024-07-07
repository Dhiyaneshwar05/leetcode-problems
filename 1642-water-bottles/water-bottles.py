class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # drank=0
        # rest_empty=0
        # drank=numBottles
        # while numBottles>0:
        #     drank+=numBottles//numExchange#new ones for exchanged bottles 
        #     rest_empty=numBottles%numExchange
        #     numBottles+=rest_empty
        # return drank
        return numBottles + (numBottles-1)//(numExchange-1)

