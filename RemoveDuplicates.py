def findDuplicates(arr):
    mp={}
    for i in arr:
        mp[i]=mp.get(i,0)+1
    duplicates=[]
    for i in mp:
        if mp[i]>1:
            duplicates.append(i)
    return duplicates
arr=list(map(int,input().split()))
print(findDuplicates(arr))