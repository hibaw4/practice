class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        p = 1
        result = []

        if zero_count > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                p *= num

        for num in nums:
            if zero_count == 1:
                if num == 0:
                    result.append(p)
                else:
                    result.append(0)
            else:
                result.append(p // num)

        return result