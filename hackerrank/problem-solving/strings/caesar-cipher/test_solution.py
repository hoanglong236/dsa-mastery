import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, s, k, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(solution.caesarCipher(s, k), expected)

    def test_example_case(self):
        self._execute_test(s="middle-Outz", k=2, expected="okffng-Qwvb")

    def test_single_character_bounds(self):
        """Test the absolute boundaries of single characters including wrapping points."""
        self._execute_test(s="a", k=1, expected="b")
        self._execute_test(s="z", k=2, expected="b")
        self._execute_test(s="A", k=3, expected="D")
        self._execute_test(s="Z", k=4, expected="D")

    def test_non_alphabetic_characters(self):
        """Ensure numeric sets and symbols remain completely unaffected."""
        self._execute_test(s="12345", k=2, expected="12345")
        self._execute_test(s="!@#$%", k=2, expected="!@#$%")

    def test_mixed_case_preservation(self):
        """Verify that lowercase and uppercase characters retain their casing independently."""
        self._execute_test(s="AbC", k=1, expected="BcD")
        self._execute_test(s="XyZ", k=2, expected="ZaB")

    def test_punctuation_and_whitespace_intervals(self):
        """Test real-world string inputs containing spaces and standard punctuation markers."""
        self._execute_test(s="Hello, World!", k=3, expected="Khoor, Zruog!")
        self._execute_test(s="Python 3.8", k=5, expected="Udymts 3.8")

    def test_exact_rotation_cycles(self):
        """Shifts that are exact multiples of 26 should return the original string unaltered."""
        self._execute_test(s="abc", k=26, expected="abc")
        self._execute_test(s="xyz", k=26, expected="xyz")
        self._execute_test(s="ABC", k=26, expected="ABC")
        self._execute_test(s="XYZ", k=26, expected="XYZ")
        self._execute_test(s="abc", k=52, expected="abc")
        self._execute_test(s="abc", k=78, expected="abc")
        self._execute_test(s="Hello World", k=0, expected="Hello World")

    def test_extreme_and_large_shifts(self):
        """Verify that massive shift values map correctly using modulo calculations."""
        self._execute_test(s="abc", k=27, expected="bcd")
        self._execute_test(s="xyz", k=99, expected="stu")

    def test_minimum_shift_bounds(self):
        """Test the absolute smallest active forward shift (k=1) across complete sequences."""
        self._execute_test(s="abc", k=1, expected="bcd")
        self._execute_test(s="xyz", k=1, expected="yza")
        self._execute_test(s="ABC", k=1, expected="BCD")
        self._execute_test(s="XYZ", k=1, expected="YZA")

    def test_maximum_single_digit_shift(self):
        """Test the largest single-digit shift possible (9) via direct and multi-rotational inputs."""
        # Baseline single-digit shift (k=9)
        self._execute_test(s="abc", k=9, expected="jkl")
        self._execute_test(s="xyz", k=9, expected="ghi")

        # Large scale shift resolving to single digit (k=35 -> 35 % 26 = 9)
        self._execute_test(s="ABC", k=35, expected="JKL")
        self._execute_test(s="XYZ", k=35, expected="GHI")

    def test_maximum_shift_bounds(self):
        """Test the edge case where the shift is exactly 25, which is the largest non-inverting cyclic shift."""
        self._execute_test(s="abc", k=25, expected="zab")
        self._execute_test(s="xyz", k=25, expected="wxy")
        self._execute_test(s="ABC", k=25, expected="ZAB")
        self._execute_test(s="XYZ", k=25, expected="WXY")

    def test_ascii_overflow_boundaries(self):
        """Test characters directly adjacent to alphabetic ranges to catch off-by-one leaks."""
        # Lower Boundaries (Floor)
        # Character 64 is '@' (immediately precedes 'A' at 65)
        self._execute_test(s="@", k=5, expected="@")
        # Character 96 is '`' (immediately precedes 'a' at 97)
        self._execute_test(s="`", k=5, expected="`")

        # Upper Boundaries (Ceiling)
        # Character 91 is '[' (immediately follows 'Z' at 90)
        self._execute_test(s="[", k=5, expected="[")
        # Character 123 is '{' (immediately follows 'z' at 122)
        self._execute_test(s="{", k=5, expected="{")

        # Combined boundary structural check
        self._execute_test(s="@`[{}]", k=10, expected="@`[{}]")


if __name__ == "__main__":
    unittest.main()
