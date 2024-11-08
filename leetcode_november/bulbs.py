A = [0,1,0,1]

switched = 0
count = 0
for i in range(len(A)):
    if switched == 0:
        if A[i] == 1:
            continue
        switched = 1
        count +=1

    elif switched == 1:
        if A[i] == 0:
            A[i] = 1
        switched = 1
        count+=1
print (count)