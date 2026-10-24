class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        indices = []

        for i in range(len(nums)):
            if nums[i] == x:
                indices.append(i)

        answer = []

        for q in queries:
            if q <= len(indices):
                answer.append(indices[q - 1])
            else:
                answer.append(-1)

        return answer