# https://leetcode.com/problems/encode-and-decode-strings/description/

class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = '' 
        for string in strs:
            encoded += string.replace('/', '//') + '/:'
        return encoded

    def decode(self, s: str) -> List[str]:
        decodedArray = []
        decodedWord = ''
        i = 0
        while i < len(s):
            if s[i: i + 2] == '//':
                decodedWord += s[i]
                i += 2
            elif s[i: i + 2] == '/:':
                i += 2
                decodedArray.append(decodedWord)
                decodedWord = ''
            else: 
                decodedWord += s[i]
                i += 1

        return decodedArray