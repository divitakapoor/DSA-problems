class Solution:
	def pushZerosToEnd(self, arr: list[int]) -> None:
    	# code here
    	n=len(arr)
    	j=0;
    	for i in range(n):
    	    if arr[i]!=0:
    	        arr[j],arr[i]=arr[i],arr[j]
    	        j+=1