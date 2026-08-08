class Solution:

    #
    # Complete the 'hackerrankInString' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts STRING s as parameter.
    #
    def hackerrankInString(self, s):
        ptn = "hackerrank"
        ptn_idx = 0

        for ch in s:
            if ch == ptn[ptn_idx]:
                ptn_idx += 1
            if ptn_idx == len(ptn):
                return "YES"
        return "NO"
