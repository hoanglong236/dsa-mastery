class Solution:

    #
    # Complete the 'gradingStudents' function below.
    #
    # The function is expected to return an INTEGER_ARRAY.
    # The function accepts INTEGER_ARRAY grades as parameter.
    #
    def gradingStudents(self, grades):
        ans = []
        for g in grades:
            if g < 38:
                ans.append(g)
            else:
                m = g % 5
                ans.append(g + (0 if m <= 2 else 5 - m))
        return ans