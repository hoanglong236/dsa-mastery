class Solution:

    #
    # Complete the 'marsExploration' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts STRING s as parameter.
    #
    def marsExploration(self, s):
        count = 0
        for i, ch in enumerate(s):
            if i % 3 == 1:
                count += int(ch != 'O')
            else:
                count += int(ch != 'S')
        return count
