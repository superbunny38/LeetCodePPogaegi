class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                decoded_string = ""
                while stack[-1] != '[':
                    top = stack.pop()
                    decoded_string = top + decoded_string
                stack.pop()
                repeat = 0
                count = 1
                while stack and ord('0') <= ord(stack[-1]) <= ord('9'):
                    num = int(stack.pop())
                    repeat += num * count
                    count *= 10
                decoded_string *= repeat
                for char in decoded_string:
                    stack.append(char)
        
        return "".join(stack)
