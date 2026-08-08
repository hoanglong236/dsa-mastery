# Sherlock and the Valid String

## Solutions

### 🚀 Quick Comparison Matrix

| Solutions & Approaches | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **s0:** Frequency Tracking | $O(n)$ | $O(1)$ |

---

### 1. Frequency Tracking

#### 💡 Intuition & Approach
Count character frequencies, group identical counts, and determine if removing at most one character can make all frequencies equal.

#### 🛠️ Technical Details
- **Pattern:** Frequency Tracking via array / hash tables
- **Time Complexity:** $O(n)$ — single linear scan over string of length $n$
- **Space Complexity:** $O(1)$ — constant auxiliary space (26‑sized array for char counts, plus a small frequency‑group map)


## Test Coverage

**Test file:** `test_solutions.py`

**Categories tested:**
- **Happy path:** equal frequencies, removal of a higher/lower frequency character, unordered & non‑consecutive inputs
- **Edge cases:** single character, repeated single character
- **Negative cases:** more than two frequency groups, two groups with no valid removal
- **Boundary scenarios:** frequency difference of 2, diff 1 with two higher‑frequency characters
- **Scale:** ~100k characters, all 26 letters equally distributed


## How to Run

```bash
python test_solutions.py
```

Expected: All tests pass. All solutions yield identical results.