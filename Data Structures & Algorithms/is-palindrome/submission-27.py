class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        l, r = 0, n-1

        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True