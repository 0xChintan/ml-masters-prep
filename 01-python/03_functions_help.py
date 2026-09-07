# ------------------------------------------------------------------
# 1. Getting Help with help()
# ------------------------------------------------------------------
# The help() function is your built-in manual for Python.
# Pass the function name (without parentheses) to see what it does.
help(round)

# Common Pitfall:
# When looking up a function, remember to pass the name of the function itself,
# and NOT the result of calling that function.
#
# What happens if we write: help(round(-2.01))?
# Python evaluates from the inside out:
# 1. First, it calculates round(-2.01) -> -2
# 2. Then, it runs help(-2) -> provides help on integers, NOT on round!

# ------------------------------------------------------------------
# 2. Rounding Examples (Positive and Negative ndigits)
# ------------------------------------------------------------------
# Positive ndigits moves RIGHT of decimal point:
print(round(3.14159))     # 3
print(round(3.14159, 2))  # 3.14

# Negative ndigits moves LEFT of decimal point:
# -1 rounds to nearest 10 (567 is closer to 570)
# -2 rounds to nearest 100 (567 is closer to 600)
print(round(567, -1))     # 570
print(round(567, -2))     # 600

# ------------------------------------------------------------------
# 3. Help on Configurable Functions (help shines here!)
# ------------------------------------------------------------------
# round() is simple, but help() shines with complex functions like print().
# It reveals useful parameters like sep (separator) and end.
help(print)

# ------------------------------------------------------------------
# 4. Defining Functions (def)
# ------------------------------------------------------------------
# Built-in functions are great, but we can only get so far with them
# before we need to start defining our own functions using 'def':

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers among a, b, and c."""
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print("Least Difference Examples:")
print(least_difference(1, 10, 100))  # 9 (closest are 1 and 10)
print(least_difference(1, 10, 10))   # 0 (10 and 10 are identical)
print(least_difference(5, 6, 7))     # 1 (closest are 5 & 6, or 6 & 7)

# ------------------------------------------------------------------
# 5. Functions That Don't Return (The 'None' value)
# ------------------------------------------------------------------
# What would happen if we didn't include the 'return' keyword?
# Python still runs the code, but it doesn't hand anything back.
# Instead, it returns a special Python value called 'None'!

def least_difference_no_return(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)  # Missing 'return'!

print("Function without return:")
result = least_difference_no_return(1, 10, 100)
print(result)  # None

# Fun fact: print() itself displays text on screen, but returns None:
mystery = print("Hello world!")
print(mystery)  # None

# ------------------------------------------------------------------
# 6. Functions Applied to Functions (Passing Functions as Arguments)
# ------------------------------------------------------------------
# In Python, functions are just like regular values (numbers or strings).
# You can pass a function into another function as an argument!

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn twice: fn(fn(arg))"""
    return fn(fn(arg))

print("Functions applied to functions:")
print(call(mult_by_five, 1))          # 5 * 1 = 5
print(squared_call(mult_by_five, 1))  # 5 * (5 * 1) = 25

# Practical Example: Custom comparison using max(..., key=fn)
# Normally, max() picks the biggest number:
print(max(100, 51, 14))  # 100

# But we can pass a function to compare numbers by a custom rule:
def mod_5(x):
    """Return remainder after dividing by 5"""
    return x % 5

# 100 % 5 = 0
# 51 % 5 = 1
# 14 % 5 = 4 (Biggest remainder!)
print(max(100, 51, 14, key=mod_5))  # 14

# --- Output ---
# Help on built-in function round in module builtins:
# 
# round(number, ndigits=None)
#     Round a number to a given precision in decimal digits.
#     The return value is an integer if ndigits is omitted or None.  Otherwise
#     the return value has the same type as the number.  ndigits may be negative.
# 
# 3
# 3.14
# 570
# 600
# Help on built-in function print in module builtins:
# 
# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.
#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     file
#       a file-like object (stream); defaults to the current sys.stdout.
#     flush
#       whether to forcibly flush the stream.
# 
# Least Difference Examples:
# 9
# 0
# 1
# Function without return:
# None
# Hello world!
# None
# Functions applied to functions:
# 5
# 25
# 100
# 14
