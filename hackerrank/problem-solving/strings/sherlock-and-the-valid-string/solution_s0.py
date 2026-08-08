class Solution:

    #
    # Complete the 'isValid' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts STRING s as parameter.
    #
    def isValid(self, s):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        groups = {}
        for count in freq:
            if count > 0:
                groups[count] = groups.get(count, 0) + 1
            if len(groups) > 2:
                return 'NO'

        if len(groups) < 2:
            return 'YES'

        g1, g2 = groups.items()

        if g1[0] > g2[0]:
            if g2 == (1, 1):
                return 'YES'
            if g1[0] - g2[0] > 1:
                return 'NO'
            return 'NO' if g1[1] != 1 else 'YES'
        else:
            if g1 == (1, 1):
                return 'YES'
            if g2[0] - g1[0] > 1:
                return 'NO'
            return 'NO' if g2[1] != 1 else 'YES'