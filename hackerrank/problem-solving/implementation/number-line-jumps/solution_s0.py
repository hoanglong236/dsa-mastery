class Solution:

    #
    # Complete the 'kangaroo' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts following parameters:
    #  1. INTEGER x1
    #  2. INTEGER v1
    #  3. INTEGER x2
    #  4. INTEGER v2
    #
    def kangaroo(self, x1, v1, x2, v2):
        if v1 == v2:
            return 'YES' if x1 == x2 else 'NO'
        d, m = divmod(x1 - x2, v2 - v1)
        return 'YES' if d >= 0 and m == 0 else 'NO'
