# CamelCase

## 💡 Intuition & Approach
In camelCase formatting, the first word starts with a lowercase letter, and every subsequent word begins with a capital letter.

We perform a single linear scan through the string: if the string is empty, we return `0`; otherwise, we start our counter at `1` and increment it by `1` for every uppercase character encountered.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | A single linear scan through the string of length $n$. |
| **Space** | $O(1)$ | Constant memory used for the counter variable. |

## 🛠️ Technical Details
- **Pattern:** Linear Scan
- **Edge Cases Handled:**
    - **Empty inputs:** Handled via an early guard clause returning `0`.
    - **Single word:** Evaluated cleanly as `1` because no uppercase transitions are triggered.
    - **Single-letter uppercase words:** Properly counts isolated capitals embedded in the text (e.g., `"isATest"`).

## 🧪 Testing
Verified using unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Validates single-character boundaries, empty inputs, and complex multi-word strings.