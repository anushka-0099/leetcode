class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s=''
        ans=[]
        for i in nums:
            s+=str(i)
            de=int(s,2)
            if de%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans