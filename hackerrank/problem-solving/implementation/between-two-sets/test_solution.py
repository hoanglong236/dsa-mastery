import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, a, b, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(solution.getTotalX(a, b), expected)

    def test_example_case(self):
        # Candidates: 4, 8, 12, 16. Checking factors: 4, 8, 16 are factors of all in b.
        self._execute_test(a=[2, 4], b=[16, 32, 96], expected=3)

    def test_no_common_factors(self):
        # LCM of a is 15. No multiples of 15 divide 7 or 11.
        self._execute_test(a=[3, 5], b=[7, 11], expected=0)

    def test_single_element_overlap(self):
        # a=[100], b=[100]. Only 100 works.
        self._execute_test(a=[100], b=[100], expected=1)

    def test_primes_in_a(self):
        # LCM(2, 3, 5) = 30. Factors of GCD(60, 90) = 30.
        # Candidates: Multiples of 30 that divide 30. (Only 30).
        self._execute_test(a=[2, 3, 5], b=[60, 90], expected=1)

    def test_large_gap(self):
        # LCM(1) = 1. GCD(100) = 100.
        # Candidates: All divisors of 100 (1, 2, 4, 5, 10, 20, 25, 50, 100).
        self._execute_test(a=[1], b=[100], expected=9)

    def test_a_contains_divisor_of_b_elements(self):
        # Example where the range is very tight.
        self._execute_test(a=[3, 6], b=[24, 36], expected=2)  # 6 and 12


if __name__ == "__main__":
    unittest.main()
