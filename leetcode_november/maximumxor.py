a ='22'
for i in map(int, a):
    print(i)
key = 3
key1 = map(int, bin(key)[2:])
for i in key1:
    print(i)
fill = len(bin(max([32]))[2:])
print(fill)
print(bin(32)[2:].zfill(fill))
print(33^29)