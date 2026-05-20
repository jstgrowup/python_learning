### **Technical Notes: Dictionary in Python**

This video explores **Dictionaries**, a versatile and widely used data structure in Python, especially in non-SQL databases like MongoDB. Unlike lists, which are ordered and sequential, dictionaries are designed for cases where order does not matter and data is accessed via custom **keys** rather than numeric indices.

---

### **1. Key Concept: Key-Value Pairs**

- **Definition:** A dictionary consists of keys (which you define) and their corresponding values.
- **Unordered:** Dictionaries are not known for sequential order; you retrieve information by knowing the specific "key".
- **Syntax:** Defined using curly braces `{}` or the `dict()` keyword.

```python
# Creating a dictionary
chai_types = {
    "masala": "spicy",
    "ginger": "zesty",
    "green": "mild"
}
```

---

### **2. Accessing and Modifying Data**

There are two primary ways to retrieve values from a dictionary:

- **Square Brackets (`[]`):** Returns the value if the key exists, but throws an error if the key is missing.
- **`.get()` Method:** Returns the value if the key exists, but returns `None` (no error) if the key is missing.
- **Updating:** To change a value, access the key and assign a new value.

```python
# Accessing
print(chai_types["masala"])      # Returns 'spicy'
print(chai_types.get("ginger"))  # Returns 'zesty'

# Modifying
chai_types["green"] = "fresh"    # Updates 'mild' to 'fresh'
```

---

### **3. Iteration (Looping)**

- **Default Behavior:** Looping directly over a dictionary iterates through its **keys**.
- **Accessing Keys and Values:** To access both simultaneously, use the `.items()` method.

```python
# Iterating over keys
for chai in chai_types:
    print(chai) # Prints masala, ginger, green

# Iterating over items (Key and Value)
for key, value in chai_types.items():
    print(key, value)
```

---

### **4. Dictionary Methods and Operations**

- **`len()`:** Returns the number of items (key-value pairs) in the dictionary.
- **Adding Items:** Simply assign a value to a brand-new key.
- **Removing Items:**
  - **`.pop(key)`:** Removes the specific key and returns its value.
  - **`.popitem()`:** Removes the last inserted item.
  - **`del`:** Deletes a specific key-value reference from memory.
- **`.clear()`:** Completely empties the dictionary.
- **`.copy()`:** Creates a shallow copy in a new memory location.

```python
# Adding a new type
chai_types["earl_grey"] = "citrus"

# Removing
chai_types.pop("ginger")     # Removes ginger
chai_types.popitem()         # Removes the last added item (earl_grey)
del chai_types["green"]      # Deletes green
```

---

### **5. Nested Dictionaries**

Dictionaries can contain other dictionaries, allowing for complex, tree-like data structures. To access nested data, chain the keys in square brackets.

```python
tea_shop = {
    "chai": {"masala": "spicy", "ginger": "zesty"},
    "tea": {"green": "mild", "black": "strong"}
}

# Accessing nested data
print(tea_shop["chai"]["ginger"]) # Returns 'zesty'
```

---

### **6. Advanced Creation Techniques**

- **Dictionary Comprehension:** Create dictionaries dynamically using loops.
- **`fromkeys()`:** Creates a new dictionary from a list of keys and a single default value.

```python
# Dictionary Comprehension (Squares)
squared_nums = {x: x**2 for x in range(6)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Using fromkeys
keys = ["masala", "ginger", "lemon"]
default_value = "delicious"
new_dict = dict.fromkeys(keys, default_value)
```
