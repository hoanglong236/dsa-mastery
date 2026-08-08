# HackerRank in a String!

## I. Solutions

### 🚀 Quick Comparison Matrix

| Solutions & Approaches | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **s0:** Two Pointers Subsequence Scan | $O(n)$ | $O(1)$ |

---

### 1. Two Pointers Subsequence Scan

#### 💡 Intuition & Approach
By using the target string `"hackerrank"` as our reference pattern, we maintain a pointer to track our current matching position within the target pattern. We then perform a single linear scan through the input string. Whenever the current character matches the expected pattern character, we increment our tracking index. If the index reaches the full length of the pattern, we immediately return `"YES"`. If the loop finishes without matching the entire pattern, we return `"NO"`.

#### 🛠️ Technical Details
- **Pattern:** Two Pointers
- **Time Complexity:** $O(n)$ — A single linear scan across the input string.
- **Space Complexity:** $O(1)$ — Auxiliary space utilized for the pattern string and the two pointers.


## II. Testing & Edge Cases

### 🧪 Testing Strategy
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.

### 🛡️ Edge Cases Coverage
- **Scale Boundaries:** Verifies the input string at minimum length ($n=10$) and evaluates system stability across massive input sizes ($n > 1000$).
- **Value Anomalies:** Enforces strict case-sensitive matching against lowercase pattern characters.
- **Structural Patterns:** Catches out-of-order sequence deviations and screens for incomplete subsequences with character omissions.