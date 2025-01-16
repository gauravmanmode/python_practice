class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        i = index + self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def range_sum(self, left, right):
        l, r, res = left + self.n, right + self.n, 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res

# Testing
st = SegmentTree([1, 3, 5, 7, 9, 11])
print(st.range_sum(1, 3))
st.update(1, 10)
print(st.range_sum(1, 3))