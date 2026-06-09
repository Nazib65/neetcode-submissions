class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        cleaned_s = ''.join(chars)

        l = 0
        r = len(cleaned_s) - 1

        while l < r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l += 1
            r -= 1
        return True