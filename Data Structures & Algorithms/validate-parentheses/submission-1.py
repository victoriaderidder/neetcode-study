class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingPairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in matchingPairs:
                if stack and stack[-1] == matchingPairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack