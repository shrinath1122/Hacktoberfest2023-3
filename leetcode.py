class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count = 0
        for i in range(1,len(arr)+1,2):
            for j in range(len(arr)-i+1):
                count += sum(arr[j:i+j])
        return count
