# Grading Students

## 💡 Intuition & Approach
We iterate through the grades and use modular arithmetic (% 5) to round up scores by checking their distance to the next multiple of 5. Grades below 38 are ignored to preserve failing statuses.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | Linear scan through the input array. |
| **Space** | $O(n)$ | Allocated space for the output array. |

## 🛠️ Technical Details
- **Pattern:** Linear Simulation / Modular Arithmetic
- **Edge Cases Handled:**
    - Failing Threshold: Grades below 38 (e.g., 35, 36, 37) are strictly protected from rounding up to a passing grade.
    - Boundary Shifts: Correctly processes critical pivot scores around the threshold (37, 38, 39, 40).
    - Extremes: Handles mathematical boundary limits gracefully (0 and 100).

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.