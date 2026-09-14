class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []
        for letter in s:
            if letter in ['(', '{', '[']:
                stack.append(letter)
            
            else: 
                if not stack: 
                    return False

                if letter == ')' and stack[-1] == '(':
                    stack.pop()

                elif letter == '}' and stack[-1] == '{':
                    stack.pop()

                elif letter == ']' and stack[-1] == '[':
                    stack.pop()

                else:
                    return False

        return len(stack) == 0
            


        