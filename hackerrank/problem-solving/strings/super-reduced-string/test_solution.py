import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, s, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(solution.superReducedString(s), expected)

    def test_example_case(self):
        """Standard case with mixed fluctuations."""
        self._execute_test("aaabccddd", "abd")

    def test_all_reducible_input(self):
        """Case where all characters form pairs and cancel out completely."""
        self._execute_test("aa", "Empty String")
    
    def test_no_reduction_possible(self):
        """Case where no two adjacent characters are identical."""
        self._execute_test("abc", "abc")
    
    def test_single_character_input(self):
        """Boundary Case: A single character cannot form a pair."""
        self._execute_test("a", "a")

    def test_long_reduction_with_scattered_duplicates(self):
        """Ensures identical characters that never become adjacent do not reduce."""
        self._execute_test("aaabbbcccaaa", "abca")
    
    def test_cascading_reduction_ripple_effect(self):
        """Critical Case: Reducing one pair makes the surrounding characters adjacent."""
        self._execute_test("baab", "Empty String")

    def test_multiple_consecutive_identical_pairs(self):
        """Ensures a long sequence of distinct pairs reduces to nothing."""
        self._execute_test("aabbccddeeffgghh", "Empty String")


if __name__ == "__main__":
    unittest.main()