class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for w in strs:
            a = sorted(w)
            b = "".join(a)
            if b in d:
                d[b].append(w)
            else:
                d[b] = [w]
        return list(d.values())