class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for c in s:
            if c in d:
                stack.append(c)
            else:
                if not stack:
                    return False
                if d[stack[-1]] != c:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False