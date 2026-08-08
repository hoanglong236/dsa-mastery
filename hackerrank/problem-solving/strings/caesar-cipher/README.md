# Caesar Cipher

## I. Solutions

### 🚀 Quick Comparison Matrix

| Solutions & Approaches | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **s0:** Modular Rotation | $O(n)$ | $O(n)$ |

---

### 1. Modular Rotation

#### 💡 Intuition & Approach
The algorithm utilizes modular arithmetic (`% 26`) to compute character transformations. Since the cipher only shifts alphabetic characters, we must precisely validate boundaries to ensure accurate rotational mapping while leaving numeric values and special characters completely unaffected.

#### 🛠️ Technical Details
- **Pattern:** Modular Arithmetic & Character Offset Mapping
- **Time Complexity:** $O(n)$ — A single linear scan across the input string.
- **Space Complexity:** $O(n)$ — A character array structure generated to store and join the transformed characters.


## II. Testing & Edge Cases

### 🧪 Testing Strategy
This problem is verified using a comprehensive suite of unit tests following the strict **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains modular baseline, edge, and boundary validation test blocks.

### 🛡️ Edge Cases Coverage
- **Scale Boundaries:** Evaluates single-character transformations, minimum active steps ($k=1$), maximum shifts ($k=99$), and full cyclic rotations ($k=26, 52, 78$).
- **Value Anomalies:** Tests and validates the maximum single-digit remainder offset scenario ($k=35 \rightarrow 9$).
- **Structural Patterns:** Guards against off-by-one leaks by testing non-alphabetic symbols immediately adjacent to the floors and ceilings of standard ASCII letters (character codes 64, 91, 96, and 123).