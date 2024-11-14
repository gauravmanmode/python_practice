A = 3
B = 1
C = [2, 2, 2]

ans, sum = 0, 0
start = 0
while(start<A):
    end = start
    while(end<A):
        sum += C[end]
        if sum > ans and sum <= B:
            ans = sum
        if sum > B:
            break
        end +=1
    sum = 0
    start+=1
print(ans)
