import math


class Solution:

    #
    # Complete the 'getTotalX' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER_ARRAY a
    #  2. INTEGER_ARRAY b
    #
    def getTotalX(self, a, b):
        a_lcm = math.lcm(*a)
        b_gcd = math.gcd(*b)

        if b_gcd < a_lcm or b_gcd % a_lcm != 0:
            return 0
        return sum(1 for x in range(a_lcm, b_gcd + 1, a_lcm) if b_gcd % x == 0)
