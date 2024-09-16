class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #convert to min 
        for i in range(len(timePoints)): 
            h,m=map(int,timePoints[i].split(":"))
            # if h==0: h=24 #for 24 hrs
            #NOTE: for this part u can use circular differece 
            #23:59 and 00:00 => 24*60-last+first= 1400-1439 =1 
            # ["12:12","00:13"]
            h=h*60
            tot=h+m
            timePoints[i]=tot%1440 
        
        #sort them out 
        timePoints.sort()

        #find min value 
        md= 1400 #24*60 = 1440 min is the max 
        for i in range(len(timePoints)-1):
            md=min(md,timePoints[i+1]-timePoints[i])
        
        md = min(md, 24 * 60 - timePoints[-1] + timePoints[0])

        return md 

            
        