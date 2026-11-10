class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

        # res = "5#Hello5#World"

    def decode(self, s: str) -> List[str]:
        # i = 0 # pointer to go through s
        # l = 0 # pointer to define start of the word
        # # length = 0 # length of the word after the delimiter #
        # # w = "" # the word that we'll construct
        # result = [] # encoded string, list of words

        # while i < len(s):
        #     w = ""
        #     length = 0
        #     if s[i] == "#":
        #         length += int(s[i+1]) # 5
        #         l += i+2 # H
        #         # a = int(length)
        #         for k in range(l, length + 2):
        #             w += s[k]
        #         result.append(w) # result = "Hello"
        #         i = l + length
        #         l = i
        # return result

        result = []
        i = 0 # scanning pointer
        start = 0 # where the current length begins

        while i < len(s):
            if s[i] == "#":
                length = int(s[start:i]) # all digits before #, so also multi digits
                word_start = i + 1
                result.append(s[word_start:word_start + length])
                i = word_start + length # to jump past the word
                start = i # where the next length starts
            else:
                i += 1
        return result

