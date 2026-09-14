class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = dict()
        letters_t = dict()

        for char in s:
            letters_s[char] = letters_s.get(char, 0) + 1

        for char in t:
            letters_t[char] = letters_t.get(char, 0) + 1

        return letters_s == letters_t

        