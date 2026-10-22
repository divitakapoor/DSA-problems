def longestSubarray(arr,k):
    n = len(arr)
    max_length = 0
    for i in range(n):
        csum = 0
        for j in range(i,n):
            csum += arr[j]
            if csum <= k:
                max_length = max(max_length, j - i + 1)
            else:
                break
    return max_length   
k=5
arr=[1,2,3,4,5]
result = longestSubarray(arr, k)
print(result)