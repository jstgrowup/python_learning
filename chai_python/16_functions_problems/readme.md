### **Technical Notes: Solving 10 Problems on Functions in Python**

This session provides a comprehensive look at Python functions, moving from basic syntax to advanced concepts like polymorphism, lambda functions, generators, and recursion.

---

### **1. Basic Function Syntax**

- **Definition:** Functions are defined using the `def` keyword (short for definition).
- **Parameters vs. Arguments:**
  - **Parameters:** The placeholders defined in the function signature (e.g., `number`).
  - **Arguments:** The actual values passed to the function during a call (e.g., `4`).
- **The `return` Keyword:** Essential for sending a result back to the caller so it can be stored in a variable. Without `return`, a function defaults to returning `None`.

```python
def square(number):
    return number ** 2

result = square(4)
print(result) # Output: 16
```

---

### **2. Multiple Parameters**

Functions can accept multiple inputs separated by commas.

```python
def add(num1, num2):
    return num1 + num2

print(add(5, 5)) # Output: 10
```

---

### **3. Polymorphism in Functions**

Polymorphism allows a single function to behave differently based on the data types of its inputs. For example, the `*` operator multiplies numbers but repeats strings.

```python
def multiply(p1, p2):
    return p1 * p2

print(multiply(8, 5))    # Output: 40
print(multiply('h', 5))  # Output: hhhhh
print(multiply(5, 'h'))  # Output: hhhhh
```

---

### **4. Returning Multiple Values**

A Python function can return multiple values simultaneously. Internally, these are typically returned as a **tuple**.

```python
import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Unpacking the returned values
area, circ = circle_stats(3)
print(f"Area: {area}, Circumference: {circ}")
```

---

### **5. Default Parameter Values**

You can assign a default value to a parameter. If the caller does not provide that argument, the default is used. This makes certain arguments optional.

```python
def greet(name="User"):
    return "Hello, " + name + "!"

print(greet("Chai")) # Output: Hello, Chai!
print(greet())       # Output: Hello, User!
```

---

### **6. Lambda Functions (Anonymous Functions)**

Lambda functions are small, one-line functions without a name. They are often used for "on-the-go" logic or within frameworks.

- **Syntax:** `lambda arguments: expression`

```python
cube = lambda x: x ** 3
print(cube(3)) # Output: 27
```

---

### **7. Variable Number of Arguments (`*args`)**

The `*args` syntax allows a function to accept any number of positional arguments. Internally, Python handles these as a **tuple**.

```python
def sum_all(*args):
    # args is a tuple (1, 2, 3...)
    return sum(args)

print(sum_all(1, 2))       # Output: 3
print(sum_all(1, 2, 3, 4)) # Output: 10
```

---

### **8. Keyword Arguments (`**kwargs`)\*\*

The `**kwargs` (keyword arguments) syntax allows a function to accept any number of named arguments. Internally, these are handled as a **dictionary**.

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Shaktiman", power="Laser")
print_kwargs(name="Shaktiman", power="Laser", enemy="Tamraj Kilvish")
```

---

### **9. Generator Functions and `yield`**

A generator function uses the `yield` keyword instead of `return`.

- **State Management:** Unlike `return`, which terminates the function, `yield` pauses the function and saves its state, allowing it to resume from where it left off.
- **Memory Efficiency:** It generates values one at a time, making it highly efficient for large datasets as it doesn't store the entire sequence in memory.

```python
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num) # Prints 2, 4, 6, 8, 10
```

---

### **10. Recursive Functions**

Recursion is a technique where a function calls itself. To avoid infinite loops, every recursive function must have an **exit strategy** (base case).

**Example: Factorial Calculation**

- **Logic:** $5! = 5 \times 4!$
- **Base Case:** If $n=0$, return $1$.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120
```
