class Solution:
    def trap(self, height: List[int]) -> int:
        # total = 0
        # for i in range(1, len(height)):
        #     l = i - 1
        #     r = i + 1
        #     if height[i] > height[l] and height[i] > height[r]:
        #         continue
        #     if height[i] == 0 and height[r] >= (height[l] - height[i]):
        #         total += min(height[l], height[r]) - height[i]
        #     elif height[i] != 0 and height[r] >= (height[l] - height[i]):

        #     if height[i] == max(height):
        #         continue

        l = 0
        r = len(height) - 1

        left_max = 0
        right_max = 0

        total = 0

        while l < r:

            if height[l] <= height[r]:

                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    total += left_max - height[l]

                l += 1

            else:

                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    total += right_max - height[r]

                r -= 1

        return total