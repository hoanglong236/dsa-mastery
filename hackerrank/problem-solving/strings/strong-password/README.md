# Strong Password

## I. Solutions

### 🚀 Quick Comparison Matrix

| Solutions & Approaches | Time | Space |
| :--- | :--- | :--- |
| **s0:** Alphanumeric Sets + Boolean Accumulation | $O(n)$ | $O(1)$ |

---

### 1. Alphanumeric Sets + Boolean Accumulation

#### 💡 Intuition & Approach
We utilize four fixed character sets to represent the mandatory password requirements. Lookups within these sets operate in $O(1)$ time. 

To optimize performance, we short-circuit redundant checks by leveraging Python's logical `or` operator across sequential states. Additionally, passing the string into a temporary set deduplicates the input characters, reducing iterations for long passwords. The solution computes the ultimate character injection requirement by using the maximum bounding limit between missing types and the overall length delta.

#### 🛠️ Technical Details
- **Pattern:** Hash Set Membership / Boolean State Tracking
- **Time** $O(n)$: We evaluate unique characters within the password string up to a maximum length of $n$.
- **Space** $O(1)$: The reference character sets remain fixed in memory. The temporary deduplication set is tightly bounded by the fixed size of the printable ASCII character pool.


## II. Testing & Edge Cases

### 🧪 Testing Strategy
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.

### 🛡️ Edge Cases Coverage
- **Scale Boundaries:** Evaluated absolute minimums including single-character string bounds and extreme character mismatches.
- **Value Anomalies:** Verified complete exhaustive compliance across every single allowed symbol, digit, and letter variation.
- **Structural Patterns:** Validated inverse tipping points where structural type omissions mathematically dominate string length deficiencies.