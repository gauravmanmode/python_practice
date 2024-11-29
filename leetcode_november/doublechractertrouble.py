A = 'aaaa'
if len(A) == 0:
    print( "")
stack = [A[0]]
for i in range(1,len(A)):
    if i == len(A) -1:
        print( A[i])
        break
    if A[i] == stack[-1]:
        stack.pop()
        continue
    stack.append(A[i])

print( ''.join(stack))
