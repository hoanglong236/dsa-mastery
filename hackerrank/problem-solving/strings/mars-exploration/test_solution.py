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
                self.assertEqual(solution.marsExploration(s), expected)

    def test_example_cases(self):
        self._execute_test("SOSSPSSQSSOR", 3)
        self._execute_test("SOSSOT", 1)
        self._execute_test("SOSSOSSOS", 0)

    def test_minimum_length_boundaries(self):
        """Verify baseline single-triplet signals for accurate match and mutation counts."""
        self._execute_test("SOS", 0)
        self._execute_test("SOA", 1)
        self._execute_test("SAS", 1)
        self._execute_test("AOS", 1)

    def test_complete_signal_corruption(self):
        """Verify behavior when every single character in the sequence fails to match."""
        self._execute_test("AAABBB", 6)

    def test_positional_mutation_patterns(self):
        """Isolate mutations at specific index positions within individual triplets to verify matching logic."""
        self._execute_test("AOSSOS", 1)
        self._execute_test("SASSOS", 1)
        self._execute_test("SOASOS", 1)
        self._execute_test("SOSAOS", 1)
        self._execute_test("SOSSAS", 1)
        self._execute_test("SOSSOA", 1)

    def test_invalid_order(self):
        """Ensure that character order is strictly enforced and any deviation counts as a mutation."""
        self._execute_test("OSSSOS", 2)
        self._execute_test("SSOSOS", 2)
        self._execute_test("OSOSOS", 3)

    def test_extreme_scale_sequences(self):
        """Ensure processing stability and accumulation accuracy across massive repeating message signals."""
        large_clean_signal = "SOS" * 33
        self._execute_test(large_clean_signal, 0)

        large_corrupted_signal = "SOS" * 32 + "OSO"
        self._execute_test(large_corrupted_signal, 3)


if __name__ == "__main__":
    unittest.main()