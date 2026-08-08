# Number Line Jumps

## 💡 Intuition & Approach
Instead of simulating the jumps step-by-step, we can determine if the kangaroos meet by solving a linear equation. The number of jumps $j$ required to meet satisfies $x_1 + j \cdot v_1 = x_2 + j \cdot v_2$, which simplifies to $j = \frac{x_1 - x_2}{v_2 - v_1}$. Using Python's `divmod`, we check if the remaining distance is perfectly divisible by the relative velocity difference ($m == 0$) and ensure that the intersection point occurs in the future ($d \ge 0$).

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(1)$ | Solved directly using basic arithmetic formulas without loops. |
| **Space** | $O(1)$ | Uses a constant amount of memory for calculation variables. |

## 🛠️ Technical Details
- **Pattern:** Mathematics / Linear Equations
- **Edge Cases Handled:**
    - **Identical Velocities ($v_1 == v_2$):** Avoids a division-by-zero error via an early guard clause, returning `"YES"` only if they start at the same position.
    - **Same Starting Position:** Correctly returns `"YES"` immediately since $d = 0$ is a valid non-negative step count.
    - **Diverging Paths ($d < 0$):** Safely catches cases where the faster kangaroo is already ahead, meaning they will never cross paths.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.