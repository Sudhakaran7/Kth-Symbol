class Solution(object):
    def kthGrammar(self, N, K):
        if K == 1:
            return 0
        if K <= (1 << (N - 2)):
            return self.kthGrammar(N - 1, K)
        else:
            return 1 - self.kthGrammar(N - 1, K - (1 << (N - 2)))

val=Solution()
N,K=map(int,input().split())
print(val.kthGrammar(N,K))
