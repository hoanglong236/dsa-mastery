# Super Reduced String

## 💡 Intuition & Approach
We utilize a Stack data structure to process the string in a single linear scan.

For each character in the input:
- Match: If the character matches the top element of the stack, an adjacent pair is identified. We perform a pop() to remove the duplicate, effectively reducing the string.
- Mismatch: If the stack is empty or the character differs from the top, we push it onto the stack.

This approach efficiently handles cascading reductions (the "ripple effect"), where removing one pair causes two previously separated identical characters to become adjacent (e.g., baab $\rightarrow$ bb $\rightarrow$ Empty String).

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | We iterate through the input string exactly once; stack operations are $O(1)$. |
| **Space** | $O(n)$ | In the worst-case scenario (no pairs found), the stack stores all $n$ characters. |

## 🛠️ Technical Details
- **Pattern:** Stack-based Linear Scan
- **Edge Cases Handled:**
    - No Reductions: Strings with no adjacent duplicates (e.g., abc) return unchanged.
    - Single Character: Minimum boundary case where no pairs can exist.
    - Ripple Effect: Cascading pairs are fully reduced to an empty state.
    - Full Reduction: Returns the specific string "Empty String" per HackerRank requirements.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.