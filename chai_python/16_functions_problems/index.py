# Function to calculate and return the square of a number 
# def square(number):
#     return number**2
# res=square(6)
# print(res)


# Create a function with  multiple parameters and returns their sum
# def add_num(a,b):
#     return a+b

# print(add_num(2,3))

# Polymorphism allows a single function to behave differently based on the data types of its inputs. For example, the * operator multiplies numbers but repeats strings.
# def multiply(p1,p2):
#     return p1*p2
# print(multiply(8,5))
# print(multiply('a',5))


# Return area and circumference
# import math
# def circle_stats(radius):
#     area= math.pi*radius**2
#     circumference=2*math.pi*radius
#     return area,circumference


# area,circumferecence=circle_stats(3)
# print(round(area,2))
# print(round(circumferecence,2))


# def greet(name="User"):
#     return "Hello" + name

# print(greet("subham"))



# 06


# cube=lambda x:x**3
# print(cube(3))


# 07
# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5,6))


# 08
# def print_kwargs(name,power):
#     print(name ,power)
# print_kwargs(name="shubham",power="lazer")
# print_kwargs(power="lazer",name="shubham")
# Same output

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_kwargs(name="Shaktiman", power="Laser")
# print_kwargs(name="Shaktiman", power="Laser", enemy="Tamraj Kilvish")




# 9

# generaor functionn that yield even numbers up to a specified limit
# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i


# even_generator(10)


# 10
# Factorial calculation

# def addNum(a,b):
#     while()