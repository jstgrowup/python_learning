### **Technical Notes: Scopes and Closures in Python**

This video provides an "investigative study" into how Python handles **Scopes** and **Namespaces**, using practical examples and a memory analogy to explain how variables are accessed across different parts of a program.

---

### **1. The Memory Analogy: Houses and Rooms**

The sources use a "house" analogy to explain memory allocation and variable visibility:

- **Global Scope:** Represents the "outside world" or the entire file. Variables declared here are accessible globally.
- **Function Scope (The House):** Creating a function is like building a distinct house in memory. Variables declared inside a function belong only to that house.
- **Nested Scope (The Rooms):** Functions defined inside other functions are like rooms inside a house. A "room" can access variables in the "house" (outer function), but the house cannot see variables restricted to a specific room.

---

### **2. Basic Scope Investigation**

Python uses **indentation** to define these scopes, unlike other languages that use curly braces. If a function cannot find a variable within its own local scope, it "climbs" up to the next level (the outer function or the global file) to look for it.

```python
username = "chai aur code" # Global variable

def func():
    # username = "chai"  # If uncommented, this is a local variable
    print(username)      # Looks for username locally; if not found, checks global

func() # If local 'chai' is missing, it prints 'chai aur code'
```

---

### **3. The `global` Keyword (And Why to Avoid It)**

You can use the `global` keyword to tell Python that a variable inside a function should refer to the one in the global namespace, allowing you to overwrite global values from within a function.

**Warning:** This is considered a **bad practice** in production code. If multiple developers manipulate the same global variables, the code becomes unreliable and difficult to debug.

```python
x = 99

def func3():
    global x
    x = 12 # Directly modifies the global variable x

func3()
print(x) # Output: 12
```

---

### **4. Closures and "Backpack Theory"**

A **Closure** occurs when a function returns another function definition.

- **The Concept:** When a function is returned, it doesn't just return the code; it carries a "backpack" containing references to all the variables it needs from its parent scope.
- **Persistent State:** Even after the outer function has finished executing, the inner function remembers the environment in which it was created.

```python
def f1():
    x = 88
    def f2():
        print(x)
    return f2 # Returns the definition, not the execution

my_result = f1()
my_result() # Output: 88 (Remembers x from the 'backpack')
```

---

### **5. Factory Functions (Practical Closures)**

Closures are often used to create **Factory Functions**, which generate customized functions based on input parameters. These are widely used in frameworks like Django.

**Example: Power Calculator Factory**
This example demonstrates how two different functions (`f` and `g`) can maintain their own unique "backpack" values for the variable `num`.

```python
def chai_coder(num):
    def actual(x):
        return x ** num
    return actual

# Creating customized functions
f = chai_coder(2) # 'num' is 2 in this backpack (Square)
g = chai_coder(3) # 'num' is 3 in this backpack (Cube)

print(f(3)) # 3 squared = 9
print(g(3)) # 3 cubed = 27
```

---

### **Key Takeaways**

- **Namespaces:** Variables with the same name can exist in different scopes (global vs. local) without interfering with each other.
- **Climbing Scopes:** Python searches for variables from the innermost scope outwards.
- **Data Types and Variables:** Understanding the value and data type inside a variable at any given time is 90% of programming.
