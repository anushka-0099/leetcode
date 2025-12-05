class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # summ=nums[:]
        s=sum(nums)
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        # return nums
        count=0
        
        for j in range(len(nums)-1):
            if (nums[j]-(s-nums[j]))%2==0:
                count+=1
        return count
