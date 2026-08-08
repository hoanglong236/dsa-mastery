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
                self.assertEqual(solution.alternate(s), expected)

    def test_example_case(self):
        """Standard case from HackerRank (beabeefeab -> babab)."""
        self._execute_test("beabeefeab", 5)

    def test_all_identical_characters(self):
        """Case where all characters are the same; no valid alternating pair can form."""
        self._execute_test("aaaa", 0)

    def test_no_valid_alternating_string_consecutive(self):
        """Case where all adjacent elements are duplicated, leaving nothing to alternate."""
        self._execute_test("aabbcc", 0)

    def test_no_valid_alternating_string_mirrored(self):
        """Case where characters are perfectly mirrored, causing inner collisions when filtered."""
        # For 'a' and 'b' -> "abba" (Invalid)
        # For 'a' and 'c' -> "acca" (Invalid)
        # For 'b' and 'c' -> "bccb" (Invalid)
        self._execute_test("abccba", 0)

    def test_multiple_valid_alternation(self):
        """Case where multiple distinct pairs yield a valid alternating string of max length."""
        # Choosing ('b', 'd') yields "bdb" (Valid, length 3)
        # Choosing ('c', 'd') yields "cdc" (Valid, length 3)
        self._execute_test("acbdbc", 3)

    def test_already_alternating_string(self):
        """Case where the input string is already perfectly alternating."""
        self._execute_test("ababab", 6)

    def test_invalidates_entire_pair_on_consecutive_duplicate(self):
        """Ensures that a character pair is completely rejected upon encountering
        consecutive duplicates, rather than just skipping the duplicate elements."""
        # For 'abaaca':
        # A flawed implementation might skip the inner duplicate 'a' and incorrectly
        # validate ('a', 'c') as "aca" (length 3).
        # The correct implementation must completely disqualify ('a', 'c'),
        # leaving ('b', 'c') -> "bc" as the max valid string with a length of 2.
        self._execute_test("abaaca", 2)

    def test_empty_string(self):
        """Edge case with an empty string input."""
        self._execute_test("", 0)

    def test_one_character_string(self):
        """Edge case with only a single character input."""
        self._execute_test("a", 0)

    def test_string_with_only_two_characters(self):
        """Boundary case with a minimal valid pair."""
        self._execute_test("ab", 2)


if __name__ == "__main__":
    unittest.main()
