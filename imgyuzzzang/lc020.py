class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        for parenthesis in s:
            if parenthesis in open :
                stack.append(parenthesis) #push
            else:
                if len(stack) == 0:
                    return False
                match = stack.pop(-1)
                if abs(ord(match) - ord(parenthesis)) > 2:
                    return False
        if len(stack) > 0:
            return False
        return True
