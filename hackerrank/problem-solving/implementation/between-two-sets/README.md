# Between Two Sets

## 💡 Intuition & Approach
The problem asks for integers that are multiples of all elements in array $A$ and factors of all elements in array $B$. 

Instead of checking numbers sequentially, we isolate the boundaries mathematically:
1. Any valid number must be a multiple of the **Least Common Multiple (LCM)** of array $A$.
2. Any valid number must be a divisor of the **Greatest Common Divisor (GCD)** of array $B$.

By computing `math.lcm(*a)` and `math.gcd(*b)`, we establish a precise range. If the cumulative GCD is not evenly divisible by the cumulative LCM, no valid integers can exist, and we short-circuit immediately. Otherwise, we efficiently step through multiples of the LCM and count how many evenly divide the GCD.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(N \log(\max(A)) + M \log(\max(B)) + \frac{\text{gcd}}{\text{lcm}})$ | Iterates through arrays $A$ and $B$ to calculate collective LCM and GCD via Euclidean steps, followed by a bounded loop checking valid multiples. |
| **Space** | $O(1)$ | Constant memory footprint. Variables are evaluated in place without additional data structures. (The final counting step uses a **generator expression** — elements are streamed and aggregated one at a time). |

## 🛠️ Technical Details
- **Pattern:** Number Theory / Mathematical Induction
- **Edge Cases Handled:**
    - **No Common Factors:** Handled via the shortcut modulo check `b_gcd % a_lcm != 0`.
    - **Single Element Overlap:** Handled correctly when $A$ and $B$ share identical boundary values.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.