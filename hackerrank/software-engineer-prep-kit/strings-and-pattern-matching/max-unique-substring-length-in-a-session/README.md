# Max Unique Substring Length in a Session

## Solutions

### 🚀 Quick Comparison Matrix

| Solutions & Approaches | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **s0:** Sliding Window + Index Tracking | $O(n)$ | $O(\min(n, \Sigma))$ |
| **s1:** String Split + Relative Distance Mapping | $O(n)$ | $O(n)$ |

---

### 1. Sliding Window + Index Tracking

#### 💡 Intuition & Approach
We scan the string linearly using a **Sliding Window**, treating `*` as a session wall that resets tracking: the hash map is cleared and the window's starting boundary (`pivot`) jumps past it. Within a session, the map tracks each character's last seen index, and `pivot` jumps past any duplicate's previous occurrence to keep the window unique.

#### 🛠️ Technical Details
- **Pattern:** Sliding Window / Hash Map Index Tracking
- **Time Complexity:** $O(n)$ — The string is processed in a single linear pass with $O(1)$ map operations.
- **Space Complexity:** $O(\min(n, 26))$ — The map stores at most the total number of unique characters ($26$) within one session.

### 2. String Split + Relative Distance Mapping

#### 💡 Intuition & Approach
This solution uses `.split('*')` to isolate session segments, then tracks each character's last seen index in a fixed-size array of 26. Within each session, if the distance between the current index and a character's last seen index exceeds the current `window_size`, that duplicate lies outside the active window, so `window_size` can safely expand without a false collision.

#### 🛠️ Technical Details
- **Pattern:** String Tokenization / Fixed-Array Relative Index Mapping
- **Time Complexity:** $O(n)$ — Splitting takes linear time, and the relative distance lookups process each character exactly once.
- **Space Complexity:** $O(n)$ — Tokenizing the string into split session segments scales proportionally with the input length.


## Test Coverage

**Test file:** `test_solutions.py`

**Categories tested:**
- **Happy path:** no asterisk, all unique characters, all same characters, sessions with asterisks, segmented sessions, single-char sessions, longest substring not at start
- **Edge cases:** empty string, only asterisks, leading/trailing asterisks, consecutive asterisks, empty session between asterisks
- **Negative cases:** duplicate requires window shrink, duplicate character outside window
- **Boundary scenarios:** single character, all letters once, all letters repeated before window ends
- **Scale:** large string without asterisks (~100k chars), large string with asterisks (>60k chars)


## How to Run

```bash
python test_solutions.py
```

Expected: All tests pass. All solutions yield identical results.