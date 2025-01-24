import sys

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [sys.maxsize] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, index, value):
        i = index + self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def range_min(self, left, right):
        l, r, res = left + self.n, right + self.n, sys.maxsize
        while l <= r:
            if l % 2 == 1:
                res = min(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = min(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

# Testing
st = SegmentTree([1, 3, 5, 7, 9, 11])
print(st.range_min(1, 3))
st.update(1, 0)
print(st.range_min(1, 3))