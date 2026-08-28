class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = sorted(set(nums))

        if len(nums) == 0:
            return 0

        current_len = 1
        max_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_len += 1
            else:
                current_len = 1

            max_len = max(max_len, current_len)
        return max_len
        
        # O(n**2) solution
        # nums = sorted(set(nums))
        # # [2,20,4,10,3,4,5] -> [2,3,4,5,10,20]

        # max_len = 1

        # if len(nums) == 0: # if we have an empty array
        #     return 0

        # for i in range(len(nums)): # we try to start from every number a consecutive sequence
        #     a = [nums[i]]
        #     j = i + 1

        #     while j < len(nums):
        #         if (nums[i] + 1) == nums[j]: # to check if the next number is consecutive
        #             a.append(nums[j])
        #             i = j # we found the next consecutive number, so now it's the next number we start at
        #             j += 1 # we look at the number after it
        #         else:
        #             break # if there isn't a consecutive number, we stop checking this sequence

        #     max_len = max(max_len, len(a)) # we update max_len
                
        # return max_len