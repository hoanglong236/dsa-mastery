import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, n, password, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(solution.minimumNumber(n, password), expected)

    def test_example_case(self):
        self._execute_test(n=3, password="Ab1", expected=3)
        self._execute_test(n=11, password="#HackerRank", expected=1)

    def test_all_requirements_met(self):
        self._execute_test(n=7, password="Ab1#xy", expected=0)

    def test_allowed_digits(self):
        # "0-9" are the allowed digits, so these should require 0 additional characters
        self._execute_test(n=6, password="Ab0#xy", expected=0)
        self._execute_test(n=6, password="Ab1#xy", expected=0)
        self._execute_test(n=6, password="Ab2#xy", expected=0)
        self._execute_test(n=6, password="Ab3#xy", expected=0)
        self._execute_test(n=6, password="Ab4#xy", expected=0)
        self._execute_test(n=6, password="Ab5#xy", expected=0)
        self._execute_test(n=6, password="Ab6#xy", expected=0)
        self._execute_test(n=6, password="Ab7#xy", expected=0)
        self._execute_test(n=6, password="Ab8#xy", expected=0)
        self._execute_test(n=6, password="Ab9#xy", expected=0)

    def test_allowed_uppercase(self):
        # "A-Z" are the allowed uppercase letters, so these should require 0 additional characters
        self._execute_test(n=6, password="aA1#xy", expected=0)
        self._execute_test(n=6, password="aB1#xy", expected=0)
        self._execute_test(n=6, password="aC1#xy", expected=0)
        self._execute_test(n=6, password="aD1#xy", expected=0)
        self._execute_test(n=6, password="aE1#xy", expected=0)
        self._execute_test(n=6, password="aF1#xy", expected=0)
        self._execute_test(n=6, password="aG1#xy", expected=0)
        self._execute_test(n=6, password="aH1#xy", expected=0)
        self._execute_test(n=6, password="aI1#xy", expected=0)
        self._execute_test(n=6, password="aJ1#xy", expected=0)
        self._execute_test(n=6, password="aK1#xy", expected=0)
        self._execute_test(n=6, password="aL1#xy", expected=0)
        self._execute_test(n=6, password="aM1#xy", expected=0)
        self._execute_test(n=6, password="aN1#xy", expected=0)
        self._execute_test(n=6, password="aO1#xy", expected=0)
        self._execute_test(n=6, password="aP1#xy", expected=0)
        self._execute_test(n=6, password="aQ1#xy", expected=0)
        self._execute_test(n=6, password="aR1#xy", expected=0)
        self._execute_test(n=6, password="aS1#xy", expected=0)
        self._execute_test(n=6, password="aT1#xy", expected=0)
        self._execute_test(n=6, password="aU1#xy", expected=0)
        self._execute_test(n=6, password="aV1#xy", expected=0)
        self._execute_test(n=6, password="aW1#xy", expected=0)
        self._execute_test(n=6, password="aX1#xy", expected=0)
        self._execute_test(n=6, password="aY1#xy", expected=0)
        self._execute_test(n=6, password="aZ1#xy", expected=0)

    def test_allowed_lowercase(self):
        # "a-z" are the allowed lowercase letters, so these should require 0 additional characters
        self._execute_test(n=6, password="Aa1#XY", expected=0)
        self._execute_test(n=6, password="Ab1#XY", expected=0)
        self._execute_test(n=6, password="Ac1#XY", expected=0)
        self._execute_test(n=6, password="Ad1#XY", expected=0)
        self._execute_test(n=6, password="Ae1#XY", expected=0)
        self._execute_test(n=6, password="Af1#XY", expected=0)
        self._execute_test(n=6, password="Ag1#XY", expected=0)
        self._execute_test(n=6, password="Ah1#XY", expected=0)
        self._execute_test(n=6, password="Ai1#XY", expected=0)
        self._execute_test(n=6, password="Aj1#XY", expected=0)
        self._execute_test(n=6, password="Ak1#XY", expected=0)
        self._execute_test(n=6, password="Al1#XY", expected=0)
        self._execute_test(n=6, password="Am1#XY", expected=0)
        self._execute_test(n=6, password="An1#XY", expected=0)
        self._execute_test(n=6, password="Ao1#XY", expected=0)
        self._execute_test(n=6, password="Ap1#XY", expected=0)
        self._execute_test(n=6, password="Aq1#XY", expected=0)
        self._execute_test(n=6, password="Ar1#XY", expected=0)
        self._execute_test(n=6, password="As1#XY", expected=0)
        self._execute_test(n=6, password="At1#XY", expected=0)
        self._execute_test(n=6, password="Au1#XY", expected=0)
        self._execute_test(n=6, password="Av1#XY", expected=0)
        self._execute_test(n=6, password="Aw1#XY", expected=0)
        self._execute_test(n=6, password="Ax1#XY", expected=0)
        self._execute_test(n=6, password="Ay1#XY", expected=0)
        self._execute_test(n=6, password="Az1#XY", expected=0)

    def test_allowed_special_characters(self):
        # "!@#$%^&*()-+" are the allowed special characters, so these should require 0 additional characters
        self._execute_test(n=6, password="Ab1!xy", expected=0)
        self._execute_test(n=6, password="Ab1@xy", expected=0)
        self._execute_test(n=6, password="Ab1#xy", expected=0)
        self._execute_test(n=6, password="Ab1$xy", expected=0)
        self._execute_test(n=6, password="Ab1%xy", expected=0)
        self._execute_test(n=6, password="Ab1^xy", expected=0)
        self._execute_test(n=6, password="Ab1&xy", expected=0)
        self._execute_test(n=6, password="Ab1*xy", expected=0)
        self._execute_test(n=6, password="Ab1(xy", expected=0)
        self._execute_test(n=6, password="Ab1)xy", expected=0)
        self._execute_test(n=6, password="Ab1-xy", expected=0)
        self._execute_test(n=6, password="Ab1+xy", expected=0)

    def test_missing_uppercase(self):
        self._execute_test(n=6, password="ab1#xy", expected=1)

    def test_missing_lowercase(self):
        self._execute_test(n=6, password="AB1#XY", expected=1)

    def test_missing_digit(self):
        self._execute_test(n=6, password="Abc#XY", expected=1)

    def test_missing_special_character(self):
        self._execute_test(n=6, password="Abc1XY", expected=1)

    def test_short_password_but_types_satisfied(self):
        """All structural type requirements are met, so only the length padding matters."""
        # Length 4, missing 2 characters to reach 6
        self._execute_test(n=4, password="Ab1#", expected=2)
        # Length 5, missing 1 character to reach 6
        self._execute_test(n=5, password="Ab1#A", expected=1)

    def test_short_password_and_missing_types(self):
        """The password is short AND missing categories. Length constraint dominates."""
        # Length 2 ("ab"), missing Uppercase, Digit, Special Char (3 types).
        # Max(3 missing types, 4 missing length) = 4
        self._execute_test(n=2, password="ab", expected=4)

        # Length 3 ("123"), missing Lower, Upper, Special Char (3 types).
        # Max(3 missing types, 3 missing length) = 3
        self._execute_test(n=3, password="123", expected=3)

        # Length 4 ("1234"), missing Lower, Upper, Special Char (3 types).
        # Max(3 missing types, 2 missing length) = 3
        self._execute_test(n=4, password="1234", expected=3)

    def test_n_mismatch_password_length(self):
        # The function should not rely on n for correctness, but it should still work if n is incorrect
        self._execute_test(n=4, password="Ab1#xy", expected=0)
        self._execute_test(n=5, password="Ab1#xy", expected=0)
        self._execute_test(n=101, password="Ab1#xy", expected=0)

    def test_single_character_password(self):
        # A single character password is missing all categories and is very short
        self._execute_test(n=1, password="a", expected=5)


if __name__ == "__main__":
    unittest.main()
