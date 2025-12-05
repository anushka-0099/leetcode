from collections import defaultdict
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # y=mx+c
        # m=dy/dx
        dic=defaultdict(list)
        st=set()
        midd=defaultdict(list)
        ans=0
        for i in range(len(points)-1):
            x1=points[i][0]
            y1=points[i][1]
            for j in range(i+1,len(points)):
                x2=points[j][0]
                y2=points[j][1]
                mx=(x1+x2)
                my=(y1+y2)
                # if (mx,my) in st:
                #     ans-=1
                # st.add((mx,my))
                dx=(x2-x1)
                dy=(y2-y1)
                if dx==0:
                    slope=1e9+7
                    c=x2
                    # dic[sl]
                else:
                    slope=dy/dx
                    c=y1-(slope*x1)
                    c=round(c,8)
                    # c=(y1*dx - x1*dy) / dx

                dic[slope].append(c)
                keyy=(mx*5000)+my
                midd[keyy].append(slope)
        
        for i in dic:
            if len(dic[i])<=1:
                continue
            d2={}
            for j in dic[i]:
                if j not in d2:
                    d2[j]=1
                else:
                    d2[j]+=1
            prev=0
            for k in d2:
                ans+=(d2[k]*prev)
                prev+=d2[k]
        # return ans
        for i in midd:
            if len(midd[i])<=1:
                continue
            d3={}
            for j in midd[i]:
                if j not in d3:
                    d3[j]=1
                else:
                    d3[j]+=1
            prev=0
            for b in d3:
                ans-=(prev*d3[b])
                prev+=d3[b]
        return ans
