class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range (len(nums)):
            complement = target - nums[i]
            # d[nums[i]] = i
            if complement in d:
                return [d[complement], i]
            else:
                d[nums[i]] = i

            # num = 3, complement: 7 - 3: 4