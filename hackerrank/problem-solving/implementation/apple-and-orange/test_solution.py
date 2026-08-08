import io
import unittest
from unittest.mock import patch
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, s, t, a, b, apples, oranges, expected_output):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                    solution.countApplesAndOranges(s, t, a, b, apples, oranges)
                    actual_output = mock_stdout.getvalue().strip().split("\n")
                    self.assertEqual(actual_output, expected_output)

    def test_example_case(self):
        self._execute_test(
            s=7,
            t=11,
            a=5,
            b=15,
            apples=[-2, 2, 1],
            oranges=[5, -6],
            expected_output=["1", "1"],
        )

    def test_no_fruits(self):
        self._execute_test(
            s=7,
            t=11,
            a=5,
            b=15,
            apples=[],
            oranges=[],
            expected_output=["0", "0"],
        )

    def test_all_fruits_on_house(self):
        self._execute_test(
            s=7,
            t=11,
            a=5,
            b=15,
            apples=[2, 3, 4],
            oranges=[-5, -4],
            expected_output=["3", "2"],
        )

    def test_all_fruits_outside_house(self):
        self._execute_test(
            s=7,
            t=11,
            a=5,
            b=15,
            apples=[-3, -4, -5],
            oranges=[6, 7],
            expected_output=["0", "0"],
        )

    def test_mixed_fruits(self):
        self._execute_test(
            s=7,
            t=11,
            a=5,
            b=15,
            apples=[-2, 2, 1, -3],
            oranges=[5, -6, 6],
            expected_output=["1", "1"],
        )

    def test_edge_case_fruits_on_boundaries(self):
        self._execute_test(
            s=7,
            t=11,
            a=5,
            b=15,
            apples=[2, 3, 6],
            oranges=[-5, -8],
            expected_output=["3", "2"],
        )


if __name__ == "__main__":
    unittest.main()
