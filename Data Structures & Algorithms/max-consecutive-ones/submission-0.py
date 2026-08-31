class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        buckets = [0]

        for num in nums:
            if num == 1:
                buckets[-1] += 1
            else:
                buckets.append(0)
        
        return max(buckets)



            
