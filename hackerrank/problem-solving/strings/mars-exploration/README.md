# Mars Exploration

## I. Solutions

### 🚀 Quick Comparison Matrix

| Solutions & Approaches | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **s0:** Modular Index Scan | $O(n)$ | $O(1)$ |

---

### 1. Modular Index Scan

#### 💡 Intuition & Approach
The expected signal consists of the message `SOS` repeated continuously. Since this target pattern repeats exactly every three characters, we can utilize modular arithmetic (`i % 3`) to verify character alignment relative to the base index. This allows us to intercept mismatched characters instantly during a single pass without allocating memory for substring extractions.

#### 🛠️ Technical Details
- **Pattern:** Modular Index Mapping & Linear Accumulation
- **Time Complexity:** $O(n)$ — A single linear scan across the input string of length $n$.
- **Space Complexity:** $O(1)$ — Constant auxiliary space utilized for an integer counter.


## II. Testing & Edge Cases

### 🧪 Testing Strategy
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.

### 🛡️ Edge Cases Coverage
- **Scale Boundaries:** Verifies a single baseline triplet ($n=3$) and stability under massive continuous sequences ($n=99$).
- **Value Anomalies:** Validates total signal corruption where all characters fail to match.
- **Structural Patterns:** Catches out-of-order sequences with inverted character alignments.