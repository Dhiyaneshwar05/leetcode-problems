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

        # M1
        # return numBottles + (numBottles-1)//(numExchange-1)

        # 9 bottles, 3 exchange 3 times, recieve 3
        # 0 bottles + 3 recieved from last time, 3 exchange, recieve 1
        # 0 bottles + 1 recieved from last time, 0 exchange, recieve 0

        # start at 9 bottles
        # + 3 recieved
        # + 1 recieved
        # = 13
        res = numBottles
        while numBottles >= numExchange:
            recieved = numBottles % numExchange
            numBottles //= numExchange
            res += numBottles
            numBottles += recieved # add the remainder to the number of bottles for the next calculation to take place
        return res
