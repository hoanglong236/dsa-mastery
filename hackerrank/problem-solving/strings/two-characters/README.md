# Two Characters

## 💡 Intuition & Approach
Instead of deleting characters, we invert the problem to find which two unique characters to **keep**.

We evaluate every possible pair of unique characters by scanning the string linearly. Using a single tracking variable (`prev`), we validate the alternating pattern on the fly and completely disqualify the pair the moment a consecutive duplicate occurs.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | The unique pairs are bounded by a constant ($\frac{26 \times 25}{2} = 325$), making the runtime scale purely linearly with string length $n$. |
| **Space** | $O(1)$ | The unique characters set and list never exceed a maximum size of 26 elements, keeping memory consumption completely constant. |

## 🛠️ Technical Details
- **Pattern:** Combinatorics / State Tracking
- **Core Insight:** Validating combinations dynamically allows early termination on duplicates, avoiding costly string allocations.
- **Edge Cases Handled:**
    - **Insufficient Elements:** Handles empty strings or single-character inputs by returning `0`.
    - **Hidden Duplicates:** Rejects a pair entirely if duplicates collide (e.g., discarding `('a', 'c')` in `"abaaca"`), preventing lazy skipping bugs.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.