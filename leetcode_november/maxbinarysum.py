C = ["1", '1', '0', '0', '1', '1', '1', '1']
M = len(C[0])
B = 2
A = 8
C = list(sorted(C, key = lambda x: int(x, 2)))
print(C)
ans = 0
for i in range(B):
    ans += 2**M - 1 - int(C[i], 2)
    print(ans)
ans += sum(list(map(lambda x : int(x, 2), C))[B:])
print(str(bin(ans)[2:]))