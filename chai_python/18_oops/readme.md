### **Technical Notes: Object-Oriented Programming (OOP) in Python**

This video uses the analogy of a **"Gujiya mold" or a "Bank form"** to explain the philosophy of Object-Oriented Programming: you create one generalized template (the **Class**) and use it to produce as many unique versions (the **Objects**) as needed.

---

### **1. Basics: Class and Object**

- **Class:** A blueprint or "generalized form". By convention, class names are **capitalized**.
- **Object (Instance):** A specific copy or "instance" created from a class.
- **Attributes:** Variables defined within a class to store data.

**Code Example:**

```python
class Car:
    # Basic class definition
    pass

# Creating an instance (Object)
my_car = Car()
```

---

### **2. The `__init__` Method and `self`**

- **`__init__` (Constructor):** A special method that is automatically called when an object is created to initialize its attributes.
- **`self` (Context):** A keyword that acts as a "telephone line" or connection between the class and the specific instance calling it. It allows the class to refer to its own attributes and methods.

**Code Example:**

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # self.brand is the class attribute
        self.model = model  # brand/model are parameters from the user

my_car = Car("Toyota", "Corolla")
print(my_car.brand) # Output: Toyota
```

---

### **3. Class Methods**

Methods are functions defined inside a class that add functionality. They must always include `self` as the first parameter to access class data.

**Code Example:**

```python
def full_name(self):
    return f"{self.brand} {self.model}"
```

---

### **4. Inheritance**

Inheritance allows a new class (**Child**) to take all the functionality of an existing class (**Parent**).

- **`super()`:** A keyword used in the child class to call methods (like `__init__`) from the parent class, avoiding code duplication.

**Code Example:**

```python
class ElectricCar(Car): # Inheriting from Car
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # Reusing parent constructor
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
```

---

### **5. Encapsulation (Private Attributes)**

Encapsulation involves hiding data so it is not directly accessible from outside the class.

- **Private Variables:** Prefixing an attribute with **two underscores (`__`)** makes it private.
- **Getter Methods:** Methods designed to allow controlled access to private data.

**Code Example:**

```python
class Car:
    def __init__(self, brand):
        self.__brand = brand # Private attribute

    def get_brand(self):
        return self.__brand + "!" # Controlled access
```

---

### **6. Polymorphism**

Polymorphism allows different classes to have methods with the same name but different behaviors.

**Code Example:**

```python
# In Car class
def fuel_type(self):
    return "Petrol or Diesel"

# In ElectricCar class
def fuel_type(self):
    return "Electric charge"
```

---

### **7. Class Variables**

Class variables are shared by all instances of a class. They are often used for tracking data across all objects, such as a counter.

**Code Example:**

```python
class Car:
    total_car = 0 # Class variable

    def __init__(self, brand):
        self.brand = brand
        Car.total_car += 1 # Accessed via Class name
```

---

### **8. Static Methods**

A **Static Method** belongs to the class rather than the instance. It is defined using the **`@staticmethod` decorator** and does not require the `self` parameter.

**Code Example:**

```python
@staticmethod
def general_description():
    return "Cars are a means of transport"
```

---

### **9. Property Decorators (Read-Only)**

Using the **`@property` decorator** allows a method to be accessed like an attribute. It is commonly used to make attributes **read-only** by not providing a setter.

**Code Example:**

```python
@property
def model(self):
    return self.__model

# Accessing: my_car.model (no parentheses needed)
```

---

### **10. Multiple Inheritance and Type Checking**

- **Multiple Inheritance:** A class can inherit from multiple parent classes simultaneously.
- **`isinstance()`:** A built-in function to check if an object is an instance of a specific class (returns `True`/`False`).

**Code Example:**

```python
# Multiple Inheritance
class ElectricCar2(Battery, Engine, Car):
    pass

# Type Checking
print(isinstance(my_tesla, Car)) # True
```
