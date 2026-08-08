class Solution:

    #
    # Complete the 'camelcase' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts STRING s as parameter.
    #
    def camelcase(self, s):
        if not s:
            return 0

        ans = 1
        for c in s:
            ans += int(c.isupper())
        return ans