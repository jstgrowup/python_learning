### **Technical Notes: Internal Working of Python (Copy, Reference Counts, Slicing)**

This video explains the internal mechanics of Python's memory management, how it treats variables as references rather than containers, and how it optimizes common data types like numbers and strings.

---

### **1. The Reference Model**

In Python, **data types belong to the memory objects**, not the variable names. A variable is merely a name (reference) that points to an object in memory.

- **Shared References:** If two variables are assigned the same value (like `10`), Python often optimizes by pointing both names to the same memory object.
- **Dynamic Typing:** Because the "type" is stored with the object in memory, a single name like `a` can point to an integer, then a string, and then a float without issue.

---

### **2. Reference Counting and Garbage Collection**

Every object in memory maintains a **reference count** (ref count) to track how many variables are pointing to it.

- **Garbage Collection (GC):** When an object's reference count drops to zero (meaning no variable uses it), Python’s garbage collector eventually removes it to free memory.
- **Optimization for Numbers/Strings:** Because small numbers and strings are used frequently, Python does not always perform **immediate garbage collection** on them, keeping them for a while in case they are needed again.
- **Checking Ref Counts:** You can use the `sys` module, but the results can be misleading due to internal interpreter optimizations.

```python
import sys
# This often returns a high, constant-looking number due to
# internal optimization loops, not just your manual assignments.
print(sys.getrefcount(244601))
```

---

### **3. Mutability and Shared References (Lists)**

Lists are **mutable**, and how you assign them determines whether they share the same memory space or become independent copies.

- **Reference Copying:** Assigning `L2 = L1` makes both names point to the **same object**. Changing one will change the other.
- **Object Re-assignment:** If you assign a completely new list to a variable (e.g., `L2 =`), it creates a **new object** with a new reference, even if the values are identical to the original list.

```python
l1 =
l2 = l1  # Shared reference
l1 = 44
print(l2)  # Returns because they point to the same list

p1 =
p2 = # New independent object created
p1 = 55
print(p2)  # Returns (unchanged)
```

---

### **4. Slicing and Copying**

To create a separate copy of a list instead of just a reference, you can use **slicing** or the `copy` module.

- **Slicing (`[:]`):** Creating a slice of a whole list generates a **new object** (a shallow copy).
- **Deep Copy:** For nested lists (lists within lists), a standard copy only goes one level deep; you must use `deepcopy` to copy all nested levels.

```python
h1 =
h2 = h1[:]  # Creates a copy via slicing
h1 = 55
print(h2)   # Returns (remains independent)

import copy
h3 = copy.copy(h1)      # Shallow copy
h4 = copy.deepcopy(h1)  # Deep copy for nested objects
```

---

### **5. Comparison Operators: `==` vs `is`**

Python provides two ways to compare variables, which is critical for understanding memory.

- **`==` (Value Equality):** Checks if the **content** (values) of the objects are the same.
- **`is` (Identity):** Checks if both variables point to the **exact same object** in memory.

```python
m =
n =

print(m == n) # True (values are the same)
print(m is n) # False (different objects in memory)
```
