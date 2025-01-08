class SegmentTreeLazy:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def update_range(self, l, r, value, node=1, start=0, end=None):
        if end is None:
            end = self.n - 1
        if self.lazy[node]:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * value
            if start != end:
                self.lazy[node * 2] += value
                self.lazy[node * 2 + 1] += value
            return
        mid = (start + end) // 2
        self.update_range(l, r, value, node * 2, start, mid)
        self.update_range(l, r, value, node * 2 + 1, mid + 1, end)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, l, r, node=1, start=0, end=None):
        if end is None:
            end = self.n - 1
        if self.lazy[node]:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0
        if start > r or end < l:
            return 0
        if start >= l and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(l, r, node * 2, start, mid) + self.query(l, r, node * 2 + 1, mid + 1, end)

# Testing
st = SegmentTreeLazy(10)
st.update_range(1, 5, 10)
print(st.query(1, 5))
st.update_range(2, 4, 5)
print(st.query(1, 5))