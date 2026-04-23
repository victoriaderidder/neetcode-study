class Solution:
    def isAlphaNum(self, c: str):
            return ('a' <= c <= 'z') or ('0' <= c <= '9')

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l].lower()):
                l += 1
            while l < r and not self.isAlphaNum(s[r].lower()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

        
        
        