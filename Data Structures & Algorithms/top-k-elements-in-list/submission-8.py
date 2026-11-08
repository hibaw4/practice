class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        # nums_s = sorted(nums)
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        #       e  o
        # d = { 1: 1,
        #       2: 2,
        #       3: 3
        # }

        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse = True))    # to sort by values from biggest to smallest
        # sorted_d = { 3: 3,
        #              2: 2,
        #              1: 1
        # }

        most_f = list(sorted_d.keys())   # [3, 2, 1]
        res = []
        for i in range(k):
            res.append(most_f[i])
        return res

        