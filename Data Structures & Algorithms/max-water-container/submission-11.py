class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # solution that could be corrected and become O(n**2), we should evaluate every pair, so we start with i1=0 and i2=1
        # area = 0
        # i1 = 0
        # i2 = 1
        # while i2 < (len(heights)):
        #     width = i2 - i1
        #     height = min(heights[i2], heights[i1])
        #     current_area = width * height
        #     area = max(area, current_area)
        #     if heights[i1] < heights[i2]:
        #         i1 += 1
        #     elif heights[i1] >= heights[i2]:
        #         i2 += 1
        # return area

        # O(n) solution, because we try to choose the maximum width, we do i1=0 and i2=len(heights)-1
        area = 0
        i1 = 0
        i2 = len(heights) - 1
        while i1 < i2:
            width = i2 - i1
            height = min(heights[i2], heights[i1])
            current_area = width * height
            area = max(area, current_area)
            if heights[i1] < heights[i2]:
                i1 += 1
            else: # or elif heights[i1] >= heights[i2]
                i2 -= 1
        return area