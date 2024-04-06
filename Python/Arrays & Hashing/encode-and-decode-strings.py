# https://leetcode.com/problems/encode-and-decode-strings/description/

# Sol 1 - O(n)

class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            res += str(len(string)) + '#' + string
        return res

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            decoded.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return decoded

# Sol 2 - O(n), worse runtime

# class Codec:
#     def encode(self, strs: List[str]) -> str:
#         encoded = '' 
#         for string in strs:
#             encoded += string.replace('/', '//') + '/:'
#         return encoded
# 
#     def decode(self, s: str) -> List[str]:
#         decodedArray = []
#         decodedWord = ''
#         i = 0
#         while i < len(s):
#             if s[i: i + 2] == '//':
#                 decodedWord += s[i]
#                 i += 2
#             elif s[i: i + 2] == '/:':
#                 i += 2
#                 decodedArray.append(decodedWord)
#                 decodedWord = ''
#             else: 
#                 decodedWord += s[i]
#                 i += 1
# 
#         return decodedArray