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
                self.assertEqual(solution.hackerrankInString(s), expected)

    def test_example_cases(self):
        self._execute_test("hereiamstackerrank", "YES")
        self._execute_test("hackerworld", "NO")

    def test_minimum_length_boundaries(self):
        """Verify baseline target strings at the absolute minimum length boundaries."""
        self._execute_test("hackerrank", "YES")
        self._execute_test("h" * 10, "NO")

    def test_extreme_scale_buffers(self):
        """Ensure processing stability and tracking accuracy inside massive input sizes."""
        self._execute_test("h" * 1000, "NO")
        self._execute_test("ha" + "x" * 1000 + "ckerrank", "YES")

    def test_invalid_order(self):
        """Catches out-of-order sequences to enforce strict chronological matching."""
        self._execute_test("hackerrnak", "NO")
        self._execute_test("hackerrakn", "NO")
        self._execute_test("hakcerrank", "NO")

    def test_character_omissions(self):
        """Verify that missing key target characters results in a failed sequence match."""
        self._execute_test("hackerank", "NO")

    def test_case_sensitivity_boundaries(self):
        """Enforce strict lowercase validation by evaluating uppercase and mixed variations."""
        self._execute_test("HACKERRANK", "NO")
        self._execute_test("HaCkErRaNk", "NO")

    def test_duplicate_character_stability(self):
        """Verify that sequence tracking advances properly when encountering clustered duplicates."""
        self._execute_test("hhaacckkerrrannkk", "YES")

    def test_non_alphabetic_noise(self):
        """Ensure the algorithm successfully ignores symbols, digits, and white-space gaps."""
        self._execute_test("1h1a1c1k1e1r1r1a1n1k", "YES")
        self._execute_test("h@a#c$k%e^r&r*a(n)k", "YES")
        self._execute_test("h a c k e r r a n k", "YES")
        self._execute_test("h\na\nc\nk\ne\nr\nr\na\nn\nk", "YES")


if __name__ == "__main__":
    unittest.main()