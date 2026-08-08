"""
Tests for Sherlock and the Valid String.

Rules: TDD-first, comment-based grouping, representative samples (not exhaustive).
"""

import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, expected, s):
        """Helper: Run test across all solutions."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(solution.isValid(s), expected)

    # =========================================================================
    # HAPPY PATH - Condition IS met, typical inputs
    # =========================================================================

    def test_equal_freq(self):
        self._execute_test("YES", "abc")
        self._execute_test("YES", "aabbcc")

    def test_remove_high_freq_char(self):
        self._execute_test("YES", "abcc")   # common freq = 1
        self._execute_test("YES", "aaccc")  # common freq > 1

    def test_remove_lone_low_freq(self):
        self._execute_test("YES", "aabbc")
        self._execute_test("YES", "abbb")

    def test_unordered_input(self):
        self._execute_test("YES", "bbba")

    def test_non_consecutive(self):
        self._execute_test("YES", "bzzcbcz")

    # =========================================================================
    # EDGE CASES - Boundaries, minimal inputs, special scenarios
    # =========================================================================

    def test_single_char(self):
        self._execute_test("YES", "a")

    def test_single_char_repeated(self):
        self._execute_test("YES", "zzzzzzzzzz")

    # =========================================================================
    # NEGATIVE CASES - Condition NOT met, invalid per problem logic
    # =========================================================================

    def test_more_than_two_freq_groups(self):
        # 3 distinct frequencies → impossible
        self._execute_test("NO", "aabbbcccc")

    def test_two_groups_no_valid_removal(self):
        self._execute_test("NO", "aabbcd")

    # =========================================================================
    # BOUNDARY - Min/max values, off-by-one scenarios
    # =========================================================================

    def test_freq_diff_of_exactly_two_invalid(self):
        self._execute_test(expected="NO", s="aaaabb")

    def test_two_higher_freq_chars(self):
        # diff=1 but two chars at higher freq → can't fix both
        self._execute_test("NO", "aaavvbbb")

    # =========================================================================
    # SCALE - Large inputs (if applicable)
    # =========================================================================

    def test_large_input(self):
        # ~100k chars, all 26 letters equally distributed
        s = "abcdefghijklmnopqrstuvwxyz" * 3846
        self._execute_test("YES", s)


if __name__ == "__main__":
    unittest.main()
