class Solution:

    #
    # Complete the 'alternate' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts STRING s as parameter.
    #
    def alternate(self, s):
        unique_chars = list(set(s))
        ans = 0

        for i in range(len(unique_chars) - 1):
            for j in range(i + 1, len(unique_chars)):
                prev = ''
                count = 0
                for ch in s:
                    if ch == unique_chars[i] or ch == unique_chars[j]:
                        if ch == prev:
                            count = 0
                            break
                        prev = ch
                        count += 1
                ans = max(ans, count)
        return ans
