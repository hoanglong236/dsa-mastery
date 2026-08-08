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
                self.assertEqual(solution.camelcase(s), expected)

    def test_example_case(self):
        self._execute_test("saveChangesInTheEditor", 5)

    def test_single_word(self):
        self._execute_test("hello", 1)

    def test_no_uppercase(self):
        self._execute_test("lowercase", 1)

    def test_empty_string(self):
        self._execute_test("", 0)

    def test_single_character(self):
        self._execute_test("a", 1)

    def test_single_uppercase_letter(self):
        self._execute_test("aB", 2)

    def test_mixed_case(self):
        self._execute_test("thisIsATest", 4)

    def test_long_string(self):
        self._execute_test("thisIsALongStringWithMultipleWords", 8)


if __name__ == "__main__":
    unittest.main()
