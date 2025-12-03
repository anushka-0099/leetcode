class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        mod0=[]
        mod1=[]
        mod2=[]
        for i in nums:
            if i%3==0:
                mod0.append(i)
            elif i%3==1:
                mod1.append(i)
            else:
                mod2.append(i)
        v=sum(nums)%3
        rem=sum(nums)
        mod1.sort()
        mod2.sort()
        if v==0:
            return sum(nums)
        elif v==1:
            if mod1:
                rem=min(rem,mod1[0])
            if len(mod2)>1:
                rem=min(rem,mod2[0]+mod2[1])
        elif v==2:
            if mod2:
                rem=min(rem,mod2[0])
            if len(mod1)>1:
                rem=min(rem,mod1[0]+mod1[1])
        return sum(nums)-rem
        