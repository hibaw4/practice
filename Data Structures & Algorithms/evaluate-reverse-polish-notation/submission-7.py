class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                s.append(int(token))
            else:
                a = s.pop()
                b = s.pop()

                if token == "+":
                    s.append(a + b)
                elif token == "-":
                    s.append(b - a)
                elif token == "*":
                    s.append(a * b)
                elif token == "/":
                    s.append(int(b / a))

        return s.pop()