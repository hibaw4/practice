class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = sorted(nums)
        result = []
        n = len(a)

        for k in range(len(a)):
            if k == 0 or a[k] != a[k-1]:
                i = k + 1
                j = n - 1
                while i < j:
                    sum = a[i] + a[j]
                    triplet = [a[k], a[i], a[j]]
                    if sum == - a[k]:
                        result.append(triplet)
                        i += 1
                        j -= 1
                        while i < j and a[i] == a[i-1]:
                            i += 1
                        while i < j and a[j] == a[j+1]:
                            j -= 1
                    elif sum > - a[k]:
                        j -= 1
                    else:
                        i += 1
        return result