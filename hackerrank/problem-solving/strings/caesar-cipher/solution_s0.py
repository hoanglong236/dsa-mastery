class Solution:

    #
    # Complete the 'caesarCipher' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts following parameters:
    #  1. STRING s
    #  2. INTEGER k
    #
    def caesarCipher(self, s, k):
        k %= 26
        ans = list(s)
        for i, ch in enumerate(ans):
            o, prefix = ord(ch), 0

            if 97 <= o and o < 123:
                prefix = 97
            elif 65 <= o and o < 91:
                prefix = 65

            if prefix != 0:
                ans[i] = chr((o - prefix + k) % 26 + prefix)

        return ''.join(ans)
