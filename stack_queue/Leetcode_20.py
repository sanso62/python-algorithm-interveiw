# Vaild Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")":
                if not len(stack) or stack.pop() != "(":
                    return False
            elif c == "}":
                if not len(stack) or stack.pop() != "{":
                    return False
            elif c == "]":
                if not len(stack) or stack.pop() != "[":
                    return False
            elif c in ["(", "{", "["]:
                stack.append(c)
        if len(stack):
            return False
        else:
            return True
