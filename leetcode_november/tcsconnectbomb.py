import math
def dist2(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

input1 = "3"
input2 = "5 2 3 4 1 1"

n = int(input1)
grid = list(map(int, input2.split()))
points = []
i = 0
while(i < len(grid)):
    points.append([grid[i], grid[i+1]])
    i+=2
points.sort()
print(points)
res = 0
p = 0 
while(p < len(points) - 1):
    res += dist2(points[p], points[p+1])
    p+=1
print(res)


