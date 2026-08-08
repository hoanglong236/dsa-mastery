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
                self.assertEqual(solution.gradingStudents(s), expected)

    def test_example_case(self):
        self._execute_test(
            s=[73, 67, 38, 33],
            expected=[75, 67, 40, 33],
        )

    def test_no_rounding(self):
        self._execute_test(
            s=[10, 35, 36, 37, 70, 75, 80],
            expected=[10, 35, 36, 37, 70, 75, 80],
        )

    def test_all_rounding(self):
        self._execute_test(
            s=[38, 48, 58],
            expected=[40, 50, 60],
        )

    def test_edge_cases(self):
        self._execute_test(
            s=[0, 37, 38, 39, 40, 100],
            expected=[0, 37, 40, 40, 40, 100],
        )


if __name__ == "__main__":
    unittest.main()
