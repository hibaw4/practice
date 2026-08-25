class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        a = list(sorted_dict.keys())
        result = slice(k)
        return a[result]