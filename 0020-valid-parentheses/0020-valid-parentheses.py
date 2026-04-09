class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range (len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                  stack.append(s[i])
            if stack:
                if (s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{'):
                    stack.pop()
            else:
                return False

        if not stack:
            return True
        else:
            return False
                