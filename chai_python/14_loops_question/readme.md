### **Technical Notes: Solving 10 Loop Problems in Python**

This session focuses on a practical, problem-solving approach to mastering loops in Python. It covers both `for` and `while` loops, keyword controls like `break` and `continue`, and internal logic like indentation and iteration.

---

### **1. Counting Positive Numbers**

**Problem:** Given a list of numbers, count how many are positive.

- **Concept:** Iterate through a list and use a counter variable.
- **Logic:** Use an `if` statement to check if the current number is greater than zero.

```python
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1

print("Final count of positive numbers is:", positive_number_count)
```

---

### **2. Sum of Even Numbers**

**Problem:** Calculate the sum of even numbers up to a given number $n$.

- **Concept:** Use `range()` to generate numbers and the modulo operator `%` to identify even numbers.
- **Range Note:** `range(1, n+1)` is used because the stop value in Python ranges is exclusive.

```python
n = 10
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += 1 # Note: Video logic adds 1 for count, or value for sum

print("Sum of even numbers is:", sum_even)
```

---

### **3. Multiplication Table with a Skip**

**Problem:** Print the multiplication table for a number up to 10, but skip the 5th iteration.

- **Key Keyword:** `continue` skips the current iteration and moves to the next one.

```python
number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{number} x {i} = {number * i}")
```

---

### **4. Reverse a String**

**Problem:** Reverse a string using a loop.

- **Logic:** Instead of standard concatenation (`reverse + char`), use `char + reverse` to build the string backward.

```python
input_string = "Python"
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print(reversed_string)
```

---

### **5. First Non-Repeated Character**

**Problem:** Given a string, find the first character that does not repeat.

- **Method:** Use the `.count()` method to check occurrences.
- **Optimization:** Use `break` to exit the loop as soon as the first unique character is found.

```python
input_string = "teeter"

for char in input_string:
    if input_string.count(char) == 1:
        print("First non-repeated character is:", char)
        break
```

---

### **6. Factorial Calculation**

**Problem:** Compute the factorial of a number using a `while` loop.

- **Definition:** $5! = 5 \times 4 \times 3 \times 2 \times 1$.
- **Logic:** Multiply the number into a result variable and decrement the number until it reaches 1.

```python
number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial value of number is:", factorial)
```

---

### **7. Input Validation**

**Problem:** Keep asking the user for input until they enter a number between 1 and 10.

- **Pattern:** Use `while True` to create an infinite loop that only exits via a `break` when the condition is met.

```python
while True:
    number = int(input("Enter value between 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks!")
        break
    else:
        print("Invalid number, try again.")
```

---

### **8. Prime Number Checker**

**Problem:** Check if a number is prime.

- **Definition:** A number greater than 1 that is only divisible by 1 and itself.
- **Logic:** Loop from 2 up to $n-1$; if any number divides it evenly, it is not prime.

```python
number = 29
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print("Is Prime:", is_prime)
```

---

### **9. List Uniqueness Checker**

**Problem:** Check if all elements in a list are unique. If a duplicate is found, print it and exit.

- **Optimization:** Use a `set` to keep track of seen items. Sets offer highly efficient membership testing (`if item in seen_set`).

```python
items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate found:", item)
        break
    unique_item.add(item)
```

---

### **10. Exponential Backoff**

**Problem:** Implement a retry strategy that doubles the wait time between retries, stopping after 5 attempts.

- **Real-world Use:** Common in APIs and password reset systems.
- **Tools:** Use `time.sleep()` to pause the program and `wait_time *= 2` to double the delay.

```python
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1} - wait time {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
```
