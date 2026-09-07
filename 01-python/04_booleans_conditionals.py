# ------------------------------------------------------------------
# 1. Booleans (True and False)
# ------------------------------------------------------------------
# A boolean represents one of two values: True or False (must be capitalized).
is_sunny = True
is_raining = False

print(type(is_sunny))  # <class 'bool'>

# ------------------------------------------------------------------
# 2. Comparison Operations:
# Comparisons return a boolean (True or False).
#
# Operation    Description
# a == b       a equal to b  (NOTE: '=' assigns, '==' compares!)
# a != b       a not equal to b
# a < b        a less than b
# a > b        a greater than b
# a <= b       a less than or equal to b
# a >= b       a greater than or equal to b
# ------------------------------------------------------------------

print("Comparison Examples:")
print(3 == 3)   # True
print(3 == 4)   # False
print(3 != 4)   # True
print(5 > 2)    # True
print(5 <= 2)   # False

# Example function: Can someone run for US President? (Need age >= 35)
def can_run_for_president(age):
    return age >= 35

print(can_run_for_president(19))  # False
print(can_run_for_president(45))  # True

# ------------------------------------------------------------------
# 3. Combining Booleans (and, or, not)
# ------------------------------------------------------------------
# 'and': True only if BOTH sides are True
# 'or':  True if AT LEAST ONE side is True
# 'not': Inverts the value (True becomes False, False becomes True)

print("Logical Operators Examples:")
age = 25
is_citizen = True

# Must be at least 18 AND a citizen to vote
can_vote = (age >= 18) and is_citizen
print(can_vote)  # True

# Free ticket if younger than 5 OR older than 65
person_age = 70
has_free_ticket = (person_age < 5) or (person_age > 65)
print(has_free_ticket)  # True

# Inverting with not
print(not True)   # False
print(not False)  # True

# ------------------------------------------------------------------
# 4. Conditionals (if, elif, else)
# ------------------------------------------------------------------
# Conditionals let our code make decisions:

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

print("Conditionals (if/elif/else) Examples:")
inspect(0)
inspect(15)
inspect(-7)
# ------------------------------------------------------------------
# 5. Boolean Conversion (bool() function)
# ------------------------------------------------------------------
# Just like int() and float(), bool() converts other types to booleans:
# - False: 0, 0.0, "" (empty text), None, [] (empty list)
# - True:  all non-zero numbers (1, -5) and non-empty text ("asf")

print("Boolean Conversion Examples:")
print(bool(1))       # True
print(bool(0))       # False
print(bool("asf"))   # True
print(bool(""))      # False

# Python automatically converts non-booleans in 'if' conditions:
if 0:
    print(0)
elif "spam":
    print("spam")    # Prints "spam" because non-empty text is True!

# --- Run Command ---
# python3 01-python/04_booleans_conditionals.py

# --- Output ---
# <class 'bool'>
# Comparison Examples:
# True
# False
# True
# True
# False
# False
# True
# Logical Operators Examples:
# True
# True
# False
# True
# Conditionals (if/elif/else) Examples:
# 0 is zero
# 15 is positive
# -7 is negative
# Boolean Conversion Examples:
# True
# False
# True
# False
# spam
