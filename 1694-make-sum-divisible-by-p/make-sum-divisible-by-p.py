class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dic={}
        # dic[0]=-1
        req=sum(nums)%p
        if req==0:
            return 0
        fin=len(nums)
        s=0
        for idx,val in enumerate(nums):
            s+=val
            s=s%p
            r=(s-req)%p
            if r==0:
                fin=min(fin,idx+1)
            if r in dic:
                fin=min(fin,idx-dic[r])
            dic[s]=idx
        return fin if fin!=len(nums) else -1


