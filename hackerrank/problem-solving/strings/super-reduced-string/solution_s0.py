class Solution:

    #
    # Complete the 'superReducedString' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts STRING s as parameter.
    #
    def superReducedString(self, s):
        if len(s) == 1:
            return s

        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack) if stack else 'Empty String'
