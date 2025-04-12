class Solution(object):
    def isValid(self, s):
        d = {"]": "[", "}": "{", ")": "(", ">": "<"}
        stack = []

        for char in s:
            if char in d.values():  
                stack.append(char)
            elif char in d:  
                if stack and stack[-1] == d[char]:
                    stack.pop()
                else:
                    return False  
        return not stack  
