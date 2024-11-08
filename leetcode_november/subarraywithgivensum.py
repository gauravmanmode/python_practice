def find_subarray_with_given_sum(A,B):
            curr = 0
            start = 0
            for i in range(len(A)):
                curr += A[i]

                if curr > B:
                    curr -= A[start]
                    start +=1
                
                if curr == B:
                    return A[start:i+1]
            return -1
            
# Example usage
arr = [5, 10, 20, 100, 105]
target_sum = 110
print(find_subarray_with_given_sum(arr, target_sum))
