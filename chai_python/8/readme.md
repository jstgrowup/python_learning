### **Technical Notes: Numbers in Depth in Python**

This video provides a deep dive into how Python handles numerical data, ranging from basic arithmetic to scientific-grade precision and complex number systems. Python is a preferred language for scientific communities like NASA because of its powerful number-handling capabilities and libraries like NumPy.

---

### **1. Core Number Types and Internal Precision**

Python treats numbers as highly precise objects. Under the hood, Python's precision for floating-point numbers is comparable to the `double` data type in C.

- **Integers & Floats:** Standard whole and decimal numbers.
- **Booleans:** Internally treated as numbers where `True` is 1 and `False` is 0.
- **Sets:** Often categorized with numbers in Python because they follow mathematical set theory.

---

### **2. Basic Operations and Best Practices**

Python supports standard operators, but **readability** and **explicit intent** are emphasized for production-grade code.

- **Arithmetic Operators:** `+` (Addition), `-` (Subtraction), `*` (Multiplication), `/` (Division), `%` (Remainder/Modulus), and `**` (Power).
- **Parentheses for Readability:** Chaining operations (e.g., `x + y * z`) should be avoided. Use parentheses to explicitly define the order of operations, which is the industry standard for clean code.
- **Operator Overloading:** The `+` operator is overloaded; it adds numbers but concatenates strings.

```python
x = 2
y = 3
z = 4

# Power operation
print(2 ** 4) # Returns 16

# Chaining with Parentheses (Recommended)
result = (x + y) * z

# Multiple assignment/results (creates a tuple)
print(x, y, z) # Returns (2, 3, 4)
```

---

### **3. Handling Large Numbers and Precision**

Python has near-infinite capability for handling large integers, unlike many other languages that fail at high powers.

- **Infinite Integer Precision:** Python can calculate extremely large numbers like `2 ** 1000` without overflow.
- **Explicit Conversion:** While Python automatically promotes results to higher precision (e.g., `40 + 2.23` becomes a float), it is better practice to use `int()` or `float()` to make your intent clear.

---

### **4. Advanced Mathematical Modules**

#### **A. The `math` Module**

Used for rounding and specific mathematical transformations.

- **`math.floor()`**: Returns the closest number below the value (bottom value).
- **`math.trunc()`**: Truncates the decimal and moves the value towards zero.

```python
import math
math.floor(3.6)   # Returns 3
math.floor(-3.5)  # Returns -4
math.trunc(2.8)   # Returns 2
math.trunc(-2.8)  # Returns -2
```

#### **B. The `random` Module**

Provides tools for randomizing data, which is essential for games and simulations.

- **`randint(start, end)`**: Generates a random integer within a range.
- **`choice(list)`**: Selects a random element from a collection.
- **`shuffle(list)`**: Randomly reorders the elements in a list in place.

```python
import random
random.randint(1, 10)
l1 = ['lemon', 'masala', 'ginger', 'mint']
random.choice(l1)
random.shuffle(l1)
```

#### **C. The `decimal` and `fractions` Modules**

Standard floating-point math can lead to precision errors (e.g., `0.1 + 0.1 + 0.1 - 0.3` may not equal `0.0` exactly).

- **`Decimal`**: Used when absolute precision is required (like in banking/finance). Values must be passed as strings to maintain precision.
- **`Fraction`**: Handles rational numbers.

```python
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Returns 0.0

from fractions import Fraction
my_fra = Fraction(2, 7)
```

---

### **5. Number Bases and Conversions**

Python can represent numbers in various bases using specific literal prefixes.

- **Binary:** Starts with `0b` (Base 2).
- **Octal:** Starts with `0o` (Base 8).
- **Hexadecimal:** Starts with `0x` (Base 16).
- **Conversion Functions:** Use `bin()`, `oct()`, or `hex()` to convert a decimal number. Alternatively, use `int('value', base)` to convert back to decimal.

---

### **6. Complex Numbers**

Python supports complex numbers using `j` to represent the imaginary unit.

```python
# Real + Imaginary
comp_num = 2 + 1j
print(comp_num * 3) # Returns (6+3j)
```

---

### **7. Comparisons and Logic**

- **Boolean Results:** Comparison operators (`<`, `>`, `==`, `!=`) return `True` or `False`.
- **Logical Operators:** `and` (requires both sides to be true) and `or` (requires only one side to be true).
- **Chaining:** Chaining comparisons like `1 < 2 < 3` is a shorthand for `1 < 2 and 2 < 3`.
- **Internal Value vs. Identity:** While `True == 1` is `True`, `True is 1` is `False` because they are different objects in memory.

---

### **8. Sets (Mathematical Collections)**

Sets are collections of unique elements used for mathematical operations like Union and Intersection.

- **Intersection (`&`)**: Finds common elements.
- **Union (`|`)**: Combines all unique elements.
- **Difference (`-`)**: Subtracts one set from another.
- **Note on Empty Sets:** An empty `{}` creates a **dictionary**. To create an empty set, you must use `set()`.

```python
set1 = {1, 2, 3, 4}
set2 = {1, 3}
print(set1 & set2) # Intersection: {1, 3}
print(set1 | {7})  # Union: {1, 2, 3, 4, 7}
```
