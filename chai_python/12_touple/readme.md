### **Technical Notes: Tuples in Python**

This video explains **Tuples** (pronounced by some as "tup-ples" and others as "too-ples"), a core Python data structure that is very similar to lists but with one critical distinction: **immutability**.

---

### **1. The Core Difference: Immutability**

The primary difference between a list and a tuple is that **lists are mutable** (can be changed in memory), while **tuples are immutable**.

- **Performance:** Once a tuple is stored in memory, it cannot be appended to or changed in place. This characteristic can often enhance performance in specific scenarios.
- **Behavior:** Like strings, once a tuple is created, the values inside it are fixed, though you can change what a variable name references.

---

### **2. Syntax and Creation**

Tuples are defined using parentheses `()`. For comparison, square brackets `[]` are for lists, and curly braces `{}` are for dictionaries.

- **Homogeneous or Heterogeneous:** They can store strings, numbers, or any other data type.

```python
# Creating a tuple with tea types
tea_types = ("Black tea", "Green tea", "Oolong tea")
```

---

### **3. Common Operations**

Most operations used with lists are also applicable to tuples because they are both sequence types.

- **Indexing:** Uses zero-based indexing to access items.
- **Negative Indexing:** Supports `[-1]` to access the last element.
- **Slicing:** Uses the `[start:stop]` syntax, where the stop index is exclusive.
- **Length:** Use the `len()` function to find the number of items.

```python
# Indexing and Slicing
print(tea_types)      # Returns 'Black tea'
print(tea_types[-1])     # Returns 'Oolong tea'
print(tea_types[1:])     # Returns ('Green tea', 'Oolong tea')

# Length
print(len(tea_types))    # Returns 3
```

---

### **4. Error Handling (Immutability Check)**

Attempting to modify a tuple after its creation will result in a **TypeError**, as tuples do not support item assignment.

```python
# This will cause an error
# tea_types = "Lemon tea"
# Output: TypeError: 'tuple' object does not support item assignment
```

---

### **5. Concatenation and Methods**

- **Joining Tuples:** You can combine two tuples using the `+` operator to create a brand-new tuple.
- **Membership Testing:** Use the `in` keyword to check for the existence of an item.
- **Counting:** Use the `.count()` method to find how many times a specific value appears.

```python
more_tea = ("Herbal tea", "Earl Grey")
all_tea = tea_types + more_tea # Creates a new combined tuple

# Membership
if "Green tea" in all_tea:
    print("I have Green tea")

# Counting
print(all_tea.count("Herbal tea")) # Returns 1
```

---

### **6. Tuple Unpacking (Unwrapping)**

A common and powerful feature of tuples is **unpacking**, where you assign the elements of a tuple to individual variables. This is frequently used when receiving data from databases.

- **Constraint:** The number of variables must match the number of items in the tuple exactly.

```python
# Unpacking the three values into three variables
black, green, oolong = tea_types

print(black) # Returns 'Black tea'
```

---

### **7. Advanced Concepts**

- **Type Checking:** You can verify an object is a tuple using the `type()` function, which will return `<class 'tuple'>`.
- **Nesting:** Like lists and strings, tuples can be nested inside one another.

```python
# Nested Tuple
nested_tuple = ("Chai", (1, 2, 3), "Coffee")
print(nested_tuple) # Returns (1, 2, 3)

# Checking Type
print(type(tea_types)) # Returns <class 'tuple'>
```
