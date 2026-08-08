"""
Tests for Max Unique Substring Length in a Session.

Rules: TDD-first, comment-based grouping, representative samples (not exhaustive).
"""

import unittest
from solution_s0 import SolutionS0
from solution_s1 import SolutionS1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
            SolutionS1(),
        ]

    def _execute_test(self, expected, s):
        """Run test across all implementations."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(
                    solution.maxDistinctSubstringLengthInSessions(s), expected
                )

    # =========================================================================
    # HAPPY PATH – typical cases, sessions with clear max unique substrings
    # =========================================================================

    def test_no_asterisk(self):
        self._execute_test(3, "abcabcbb")

    def test_all_unique_characters(self):
        self._execute_test(7, "abcdefg")

    def test_all_same_characters(self):
        self._execute_test(1, "aaaaaa")

    def test_sessions_with_asterisks(self):
        # "abc" -> 3, "de" -> 2, max = 3
        self._execute_test(3, "abc*de")

    def test_segmented_sessions(self):
        # "abcb" -> 3 ("abc"), "xyz" -> 3, max = 3
        self._execute_test(3, "abcb*xyz")

    def test_single_char_sessions(self):
        self._execute_test(1, "a*b*c*d*e")

    def test_longest_substring_not_at_start(self):
        self._execute_test(3, "pwwkew")  # "wke" or "kew"
        self._execute_test(4, "abcad")  # "bcad"

    # =========================================================================
    # EDGE CASES – empty, boundaries, asterisk placement
    # =========================================================================

    def test_empty_string(self):
        self._execute_test(0, "")

    def test_only_asterisks(self):
        self._execute_test(0, "****")
        self._execute_test(0, "*")

    def test_leading_trailing_asterisks(self):
        self._execute_test(3, "*abc")
        self._execute_test(3, "abc*")
        self._execute_test(3, "*abc*")

    def test_consecutive_asterisks(self):
        # sessions: "a", "", "b" → max 1
        self._execute_test(1, "a**b")

    def test_session_empty_between_asterisks(self):
        # sessions: "" (empty), "a", "" (empty) → max 1
        self._execute_test(1, "*a*")

    # =========================================================================
    # NEGATIVE / LOGIC CASES – ensuring window sliding works correctly
    # =========================================================================

    def test_duplicate_requires_window_shrink(self):
        # "abba" → "ab" or "ba" length 2
        self._execute_test(2, "abba")

    def test_duplicate_character_outside_window(self):
        # "tmmzuxt" → 5 ("mzuxt")
        self._execute_test(5, "tmmzuxt")

    # =========================================================================
    # BOUNDARY – minimum / maximum possible unique length (1 / 26 letters)
    # =========================================================================

    def test_single_character(self):
        self._execute_test(1, "z")

    def test_all_letters_once(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        self._execute_test(26, s)

    def test_all_letters_repeated_before_window_ends(self):
        # first repeat invalidates the start; max still 26
        s = "abcdefghijklmnopqrstuvwxyza"
        self._execute_test(26, s)

    # =========================================================================
    # SCALE – large inputs (time complexity O(n) per session)
    # =========================================================================

    def test_large_string_without_asterisks(self):
        # 100 000 characters, repeating the alphabet
        s = "abcdefghijklmnopqrstuvwxyz" * 4000  # 104 000 chars
        self._execute_test(26, s)

    def test_large_string_with_asterisks(self):
        # many small sessions + one long session
        parts = ["a" * 1000, "b" * 1000, "c" * 1000]
        s = "*".join(parts) + "*" + ("xyz" * 20000)  # final session length 60000
        # each "a"*1000 has max 1, "b"*1000 1, "c"*1000 1, long session 3
        self._execute_test(3, s)


if __name__ == "__main__":
    unittest.main()
