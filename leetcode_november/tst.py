def soln():
    nums = [1,2,5,6,7,8,9,11]
    nums.sort()
    print(nums)
    cnt = []
    count=1

    for i in range(1,len(nums)):
        print(i)
        if nums[i]==nums[i-1]+1:
            count+=1
        else:
            cnt.append(count)
            count = 1
    cnt.append(count)
    return max(cnt)
     


print(soln())