class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = sorted(nums)
        result = []
        n = len(a)

        for k in range(len(a)):
            i = k + 1
            j = n - 1
            while i < j:
                sum = a[i] + a[j]
                if sum == -a[k]:
                    if [a[k], a[i], a[j]] not in result:
                        result.append([a[k], a[i], a[j]])
                        i += 1
                        j -= 1
                    else:
                        i += 1
                        j -= 1
                elif sum > -a[k]:
                    j -= 1
                elif sum < -a[k]:
                    i += 1
        return result