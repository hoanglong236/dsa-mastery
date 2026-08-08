import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, x1, v1, x2, v2, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(solution.kangaroo(x1, v1, x2, v2), expected)

    def test_example_case(self):
        self._execute_test(x1=0, v1=3, x2=4, v2=2, expected="YES")

    def test_example_case_2(self):
        self._execute_test(x1=0, v1=2, x2=5, v2=3, expected="NO")

    def test_same_start_and_velocity(self):
        self._execute_test(x1=0, v1=2, x2=0, v2=2, expected="YES")

    def test_same_start_different_velocity(self):
        self._execute_test(x1=0, v1=2, x2=0, v2=3, expected="YES")

    def test_different_start_same_velocity(self):
        self._execute_test(x1=0, v1=2, x2=1, v2=2, expected="NO")

    def test_different_start_and_velocity_meeting(self):
        self._execute_test(x1=0, v1=3, x2=4, v2=2, expected="YES")

    def test_different_start_and_velocity_not_meeting(self):
        self._execute_test(x1=0, v1=2, x2=4, v2=3, expected="NO")


if __name__ == "__main__":
    unittest.main()
