class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        t = [[] for _ in range(4*n)]
        def build(v, tl, tr, A):
            if tl ==tr:
                t[v].append(A[tl])
            else:
                tm = (tl +tr) //2
                build(2*v, tl, tm, A)
                build(2*v+1, tm+1, tr, A)
                t[v] = sorted(t[2*v] + t[2*v+1])
        
        build(1,0,n-1, A)

        def query(v, tl, tr, l, r, k):
            if l>r:
                return 0
            if l == tl and r==tr:
                from bisect import bisect_left
                index = bisect_left(t[v], k)
                return len(t[v]) - index
            tm = (tl+tr) //2
            left = query(2*v, tl, tm, l, min(r,tm), k)
            right = query(2*v+1, tm+1, tr, max(l,tm+1), r, k)
            return left + right

        res = []
        for [L,R,K] in B:
            res.append(query(1,0,n-1,L-1,R-1,K))
        return res


