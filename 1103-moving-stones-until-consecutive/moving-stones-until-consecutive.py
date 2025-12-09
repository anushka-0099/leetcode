class Solution:
    
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        minm=0
        maxm=0
        # x=min(a,b,c)
        x=[a,b,c]
        x.sort()
        if x[2]-x[1]==1 and x[1]-x[0]==1:
            return [0,0]
        if ((x[2]-x[1]==1 or x[1]-x[0]==1) and (x[2]-x[1]>1 or x[1]-x[0]>1)):
            minm=1
            maxm=x[2]-x[1] if x[2]-x[1]>1 else x[1]-x[0]
            maxm-=1
        elif ((x[2]-x[1]==2 or x[1]-x[0]==2) and (x[2]-x[1]>1 or x[1]-x[0]>1)):
            minm=1
            maxm=x[2]-x[1] if x[2]-x[1]>2 else x[1]-x[0]
        else:
            minm=2
            maxm=(x[2]-x[1]-1)+(x[1]-x[0]-1)
        return [minm,maxm]
        
        