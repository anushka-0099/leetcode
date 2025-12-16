class Solution:
    def minOperations(self, n: int) -> int:
        # def f(num):
        #     if num==0:
        #         return 0
        #     nchange=f(num)
        #     for i in range(len(bin(num)))
        # 1111
        # 15
        # +1=16
        # ->2operns
        # 1110  14  #even ->10111  
        c=0
        while n>0:
            if n%2==0:
                n>>=1
            elif (n&2)>0:
                n+=1
                c+=1
            else:  
                #this means that combn is 111101
                n>>=2
                c+=1
        return c