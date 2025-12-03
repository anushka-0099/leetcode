class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # my intuition is to do postorder traversal and then sum and send to root and then chech if it is divisible 
        # arr=[0]*(n)
        arr=values[:]
        comp=0
        # def dfs(node,par):
        #     nonlocal comp
        #     if not node:
        #         return
        #     if node.left:
        #         dfs(node.left,node)
        #     if node.right:
        #         dfs(node.right,node)
        adj=[[]for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        # start=set()
        # for i in adj:
        vis=[-1]*n
        q=deque()
        stack=[]
        q.append((0,-1))
        while q:
            a,par=q.popleft()
            stack.append((a,par))
            vis[a]=1
            for z in adj[a]:
                if vis[z]==-1:
                    q.append((z,a))
            # if a.left:
            #     q.append((a.left,a))
            # if a.right:
            #     q.append((a.right,a))
        # return stack.pop()
        while stack:
            node,p=stack.pop()
            if arr[node]%k==0:
                arr[node]=0
                comp+=1
            else:
                arr[p]+=arr[node]
        return comp
