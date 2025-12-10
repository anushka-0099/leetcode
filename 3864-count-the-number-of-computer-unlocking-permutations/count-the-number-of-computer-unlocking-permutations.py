class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        start=complexity[0]
        if complexity.count(start)>1:
            return 0
        complexity.sort()
        if complexity[0]!=start:
            return 0
        return (math.factorial(len(complexity)-1))%((10**9)+7)
