class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            a = ''.join(sorted(strs[i]))       
            # i=0, act i=1, opst i=2, opst, i=3, act, i=4, opst, i=5, aht
            if a in d:
                d[a].append(strs[i])
            else:
                d[a] = [strs[i]]                 

#       {'act': ['act', 'cat'],
#        'opst': ['pots', 'tops', 'stop'],
#        'aht': ['hat']
#       }

        return list(d.values())   # [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]