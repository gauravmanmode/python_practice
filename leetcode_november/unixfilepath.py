A = '/home//foo/'
A = A.split('/')[1:-1]
print(A)
stack = []
for i in A:
    if i == '..':
        if len(stack) != 0:
            stack.pop()
    elif i == '.':
        pass
    else:
        stack.append(i)
# return '/' +'/'.join(stack)
