class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_sorted = sorted(s)
        # t_sorted = sorted(t)
        # for s in s_sorted :
        #     for t in t_sorted:
        #         if s != t:
        #             return False
        # return True
        if sorted(t) == sorted(s):
            return True
        return False
