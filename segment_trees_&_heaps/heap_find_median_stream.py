import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        return -self.small[0] if len(self.small) > len(self.large) else (-self.small[0] + self.large[0]) / 2

# Testing
mf = MedianFinder()
for num in [5, 3, 8, 2]:
    mf.add_num(num)
    print(mf.find_median())