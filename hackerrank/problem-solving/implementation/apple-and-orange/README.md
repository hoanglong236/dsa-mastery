# Apple and Orange

## 💡 Intuition & Approach
We simulate the fruit fall by calculating the landing position for each apple and orange. By checking if the resulting position ($tree\_position + distance$) falls within the inclusive range $[s, t]$, we determine the total count of fruits that land on the house.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n + m)$ | We perform a single linear scan through the $n$ apples and $m$ oranges. |
| **Space** | $O(1)$ | We only use a constant amount of extra space for the counting variables. |

## 🛠️ Technical Details
- **Pattern:** Linear Simulation
- **Edge Cases Handled:**
    - Empty Input: Correctly handles cases where the apple or orange arrays are empty.
    - Boundary Conditions: Includes fruits that land exactly on the edges of the house ($s$ or $t$).
    - Large Distances: Correctly ignores fruits that fall far beyond the house in either direction.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Employs `unittest.mock.patch` to intercept `sys.stdout`, validating terminal output against expected fruit counts across standard and edge scenarios.