class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = {}, {}

        for s1 in s:
            if s1 not in ds:
                ds[s1] = 1
            else:
                ds[s1] += 1

        for t1 in t:
            if t1 not in dt:
                dt[t1] = 1
            else:
                dt[t1] += 1

        if ds == dt:
            return True
        else:
            return False
