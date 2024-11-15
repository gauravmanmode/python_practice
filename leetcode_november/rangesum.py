class Solution:
    def rangeSum(self, A, B):
        leftsum = [A[0]]
        for i in range(1,len(A)):
            leftsum.append(leftsum[i-1]+A[i])
            res = []
        for [i,j] in B:
            if i==0:
                res.append(leftsum[j])
            else:
                res.append(leftsum[j]-leftsum[i-1])
        return res
    
def main():
    A = [1, 2, 3, 4, 5]
    B = [[0, 3], [1, 2]]
    print(Solution().rangeSum(A,B))

if __name__ == "__main__":
    main()