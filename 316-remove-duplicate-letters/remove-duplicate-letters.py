class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        lastind = {}
        visited = set()

        for i in range(len(s)):
            lastind[s[i]] = i

        for i in range(len(s)):
            if s[i] not in visited:
                while stack and s[i] < stack[-1] and i < lastind[stack[-1]]:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])

        return "".join(stack)