f = [-1] * 20
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        global f
        f[0], f[1], f[2] = 1,1,2
        return self.func(A)
    def func(self, A):
        if f[A] != -1:
            return f[A]
        else:
            f[A] = self.func(A-1) + self.func(A-2) + self.func(A-3) + A
        return self.func(A-1) + self.func(A-2) + self.func(A-3) + A
    
def main():
    A = 4
    print(Solution().solve(A))

if __name__ == '__main__':
    main()