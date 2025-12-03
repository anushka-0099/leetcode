class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            rem=i%3
            val=i
            k=i+rem
            x=k-3
            xy=val-x
            count+=min(xy,rem)
        return count
        
        