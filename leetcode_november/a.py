str = 'PAYPALISHIRING'
numRows = 3

ans = ''
k = numRows*2-2
i=0
ans += str[::k]
start = 0
for s in range(1,numRows-1):
    i+=2
    start += 1
    cur = start
    while(True):
        ans += str[cur]
        cur += k-i
        if cur >= len(str):
            break             
        ans += str[cur]
        cur += i
        if cur >= len(str):
            break  

ans += str[numRows -1::k]

print(ans)
    