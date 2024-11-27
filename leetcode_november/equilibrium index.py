class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        leftsum = 0
        
        rightsum = sum(A)
        for i in range(0, len(A)):
            rightsum -= A[i]
            if leftsum == rightsum:
                return i
            leftsum += A[i]
        return -1
    
def main():
    B = [-7, 1, 5, 2, -4, 3, 0]
    A = Solution()
    print(A.solve(B))

if __name__ == "__main__":
    main()