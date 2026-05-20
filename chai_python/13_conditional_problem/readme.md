### **Technical Notes: Solving Conditional Problems in Python**

This session focuses on a "problem-first" approach to learning Python, demonstrating how to convert real-world logic into functional code using conditional statements.

---

### **1. Core Concepts: Inputs and Indentation**

- **User Input:** The `input()` function captures user data as a **string**. To perform math or comparisons, you must explicitly convert it using `int()`.
- **Indentation:** Python uses white space (usually 2 or 4 spaces) instead of curly braces to define code blocks. Consistency is mandatory.
- **Logical Operators:**
  - `and`: Both conditions must be true.
  - `or`: At least one condition must be true.
- **Exiting a Program:** Use the `exit()` function to stop the execution of a script prematurely if a specific condition (like an invalid input) is met.

---

### **2. Practical Problem Solving**

#### **Problem 1: Age Group Categorization**

Classify a person based on their age: Child (<13), Teenger (13-19), Adult (20-59), or Senior (60+).

```python
age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

_Note: Using `elif` ensures that once a condition is met, the rest are skipped._

#### **Problem 2: Movie Ticket Pricing**

Standard price is $12 for adults (18+) and $8 for children. Everyone gets a $2 discount on Wednesdays.
**Advanced Syntax (Ternary-like):**

```python
age = 26
day = "Wednesday"

# One-liner conditional assignment
price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2  # Equivalent to price = price - 2

print(f"Ticket price for you is ${price}")
```

_The instructor introduces an "interesting" syntax for assigning values based on a condition in a single line._

#### **Problem 3: Grade Calculator**

Assign grades based on scores: A (90-100), B (80-89), C (70-79), D (60-69), F (<60).

```python
score = 105

if score > 100:
    print("Please verify your grade again")
    exit() # Stops the program for invalid scores

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

_Including a check for scores above 100 demonstrates defensive programming._

#### **Problem 4: Fruit Ripeness Checker**

Determine ripeness based on color for a specific fruit.

```python
fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
```

_This uses **nested conditionals** to first verify the fruit type before checking its color._

#### **Problem 5: Weather Activity Suggestion**

```python
weather = "Sunny"

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"
```

#### **Problem 6: Transportation Mode Selection**

```python
distance = 5

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"
```

#### **Problem 7: Coffee Customization**

```python
order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"
```

#### **Problem 8: Password Strength Checker**

Checks strength based on length: <6 (Weak), 6-10 (Medium), >10 (Strong).

```python
password = "secure123"
password_len = len(password) # Optimization: calculate length once

if password_len < 6:
    strength = "Weak"
elif password_len <= 10:
    strength = "Medium"
else:
    strength = "Strong"
```

_Calculating `len()` once in a variable is a performance optimization for production-level code._

#### **Problem 9: Leap Year Checker**

A year is a leap year if it is divisible by 4 but not by 100, **unless** it is also divisible by 400.

```python
year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")
```

_This problem demonstrates complex logical chaining using `and`, `or`, and the modulo operator `%` to check for remainders._

---

### **3. Practice Assignment**

**Problem 10: Pet Food Recommendation**

- **Dog (< 2 years):** Pappy food.
- **Dog (> 2 years):** Adult food.
- **Cat (> 5 years):** Senior cat food.
- **Cat (< 5 years):** Junior cat food.
