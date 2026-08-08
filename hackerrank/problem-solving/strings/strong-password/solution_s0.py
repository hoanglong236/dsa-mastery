class Solution:

    #
    # Complete the 'minimumNumber' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. STRING password
    #
    def minimumNumber(self, n, password):
        cur_len = len(password)
        miss_len = 0 if cur_len >= 6 else 6 - cur_len

        numbers = set("0123456789")
        lower_case = set("abcdefghijklmnopqrstuvwxyz")
        upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        special_characters = set("!@#$%^&*()-+")

        has_number = False
        has_lower = False
        has_upper = False
        has_special = False

        for ch in set(password):
            has_number = has_number or ch in numbers
            has_lower = has_lower or ch in lower_case
            has_upper = has_upper or ch in upper_case
            has_special = has_special or ch in special_characters
            if has_number and has_lower and has_upper and has_special:
                break

        total_miss_types = 4 - has_number - has_lower - has_upper - has_special
        return max(miss_len, total_miss_types)
