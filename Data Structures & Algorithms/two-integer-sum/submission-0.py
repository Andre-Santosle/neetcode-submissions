class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            dif = target - num
            if dif in map:
                return [map[dif],  i]
            map[num] = i

