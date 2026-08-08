class SolutionS0:

    #
    # Complete the 'maxDistinctSubstringLengthInSessions' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts STRING sessionString as parameter.
    #
    def maxDistinctSubstringLengthInSessions(self, sessionString):
        idx_dict = {}
        ans = 0
        pivot = 0
        for i, ch in enumerate(sessionString):
            if ch == "*":
                idx_dict = {}
                pivot = i + 1
                continue
            if ch in idx_dict:
                pivot = max(pivot, idx_dict[ch] + 1)

            ans = max(ans, i - pivot + 1)
            idx_dict[ch] = i
        return ans
