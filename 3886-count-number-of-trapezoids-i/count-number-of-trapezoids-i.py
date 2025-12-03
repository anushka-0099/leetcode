import math
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # return 0
        mod=((10**9)+7)
        points.sort(key=lambda x:[x[1],x[0]])
        dic={}
        for x,y in points:
            if y not in dic:
                dic[y]=1
            else:
                dic[y]+=1
        arr=[]
        ans=0
        for i in dic:
            if dic[i]!=1:
                arr.append(dic[i])
        # return arr
        for i in range(len(arr)):
            arr[i]=math.comb(arr[i],2)
        suff=arr[:]
        # suff[-1]=arr[-1]
        for i in range(len(suff)-2,-1,-1):
            suff[i]+=suff[i+1]
        for i in range(len(arr)-1):
            v=arr[i]*suff[i+1]
            ans+=v
            ans=ans%mod
        return ans
        #     for j in range(i+1,len(arr)):
        #         a=math.comb(arr[j],2)
        #         ans+=(v*a)
        #         ans=ans%mod
        # return ans%mod

    