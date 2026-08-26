class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + '#' + s

        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the #
            while s[j] != "#":
                j += 1

            # Get the length
            length = int(s[i:j])

            # Get the actual word
            word = s[j + 1:j + 1 + length]

            result.append(word)

            # Move to the next encoded word
            i = j + 1 + length

        return result

# strs = ["hello", "world"]
# encoding: 5#hello3#world length + # + word
# decoding: we see the length of the word to define the word and the separator between words