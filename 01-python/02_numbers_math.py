# 1. Number Types: int (whole numbers) and float (decimals)
spam_amount = 0
print(type(spam_amount))  # <class 'int'>
print(type(19.95))        # <class 'float'>

# ------------------------------------------------------------------
# Basic Arithmetic in Python:
# We've seen + for addition and * for multiplication.
# Here are the rest of the basic calculator operators:
#
# Operator   Name            Description
# a + b      Addition        Sum of a and b
# a - b      Subtraction     Difference of a and b
# a * b      Multiplication  Product of a and b
# a / b      True division   Quotient of a and b
# a // b     Floor division  Quotient of a and b, removing fractional parts
# a % b      Modulus         Integer remainder after division of a by b
# a ** b     Exponentiation  a raised to the power of b
# -a         Negation        The negative of a
# ------------------------------------------------------------------
print("Basic Arithmetic Examples:")
# 2. Examples using a = 5 and b = 2:
a = 5
b = 2

# Addition
print(a + b)   # 5 + 2 = 7

# Subtraction
print(a - b)   # 5 - 2 = 3

# Multiplication
print(a * b)   # 5 * 2 = 10

# True division (always returns a float with decimals)
print(a / b)   # 5 / 2 = 2.5

# Floor division (chops off the decimal part)
print(a // b)  # 5 // 2 = 2

# Modulus (the remainder: 5 divided by 2 gives remainder 1)
print(a % b)   # 5 % 2 = 1

# Exponentiation (5 to the power of 2, or 5 * 5)
print(a ** b)  # 5 ** 2 = 25

# Negation (makes a number negative)
print(-a)      # -5

# ------------------------------------------------------------------
# 3. Order of Operations (PEMDAS):
# Python follows the math rules we learned in primary school:
#   P - Parentheses () first
#   E - Exponents **
#   M / D - Multiplication * and Division / (left to right)
#   A / S - Addition + and Subtraction - (left to right)
# ------------------------------------------------------------------
print("Order of Operations (PEMDAS) Examples:")
# Example 1: Multiplication happens before addition
print(-3 + 4 * 2)      # -3 + 8 = 5

# Example 2: Parentheses () force this to happen first
print((-3 + 4) * 2)    # 1 * 2 = 2

# Example 3: Why parentheses matter (calculating total height in meters)
hat_height_cm = 25
my_height_cm = 190

# Without (): divides 190 / 100 first (1.9), then adds 25 -> 26.9 (Wrong!)
print(hat_height_cm + my_height_cm / 100)

# With (): adds (25 + 190 = 215) first, then divides by 100 -> 2.15 (Correct!)
print((hat_height_cm + my_height_cm) / 100)

# ------------------------------------------------------------------
# 4. Built-in Functions for Numbers:
# Python comes with ready-to-use math functions:
# - min() and max(): return the smallest and largest values
# - abs(): returns the absolute value (removes negative signs)
# - int() and float(): convert types into whole numbers or decimals
# ------------------------------------------------------------------
print("Built-in Functions Examples:")

# min and max (minimum and maximum)
print(min(1, 2, 3))    # 1
print(max(1, 2, 3))    # 3

# abs (Absolute value: distance from zero, always positive)
print(abs(32))         # 32
print(abs(-32))        # 32

# int and float (Type conversion)
print(int(3.14))       # Drops decimals -> 3
print(int('807') + 1)  # Converts text '807' to int -> 808
print(float(10))       # Converts int to decimal -> 10.0
print(float('3.14'))   # Converts text '3.14' to decimal -> 3.14

# --- Run Command ---
# python3 01-python/02_numbers_math.py

# --- Output ---

# <class 'int'>
# <class 'float'>
# Basic Arithmetic Examples:
# 7
# 3
# 10
# 2.5
# 2
# 1
# 25
# -5
# Order of Operations (PEMDAS) Examples:
# 5
# 2
# 26.9
# 2.15
# Built-in Functions Examples:
# 1
# 3
# 32
# 32
# 3
# 808
# 10.0
# 3.14
