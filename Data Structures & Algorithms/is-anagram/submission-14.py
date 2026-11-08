class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        for cs in s:
            if cs not in ds:
                ds[cs] = 1
            else:
                ds[cs] += 1

        dt = {}
        for ct in t:
            if ct not in dt:
                dt[ct] = 1
            else:
                dt[ct] += 1

        if ds == dt:
            return True
        return False