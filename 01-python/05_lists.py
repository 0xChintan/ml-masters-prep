# ------------------------------------------------------------------
# Setup: Lists and Nested Lists (Lists containing other lists)
# ------------------------------------------------------------------
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Lists can contain other lists (e.g. hands of playing cards):
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read):
# hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

# ------------------------------------------------------------------
# 1. Indexing (Accessing items by position)
# ------------------------------------------------------------------
# Python is 0-indexed (starts at 0).
# Negative indices count backwards from the end (-1 is the last item).

print("1. Indexing Examples:")
print(planets[0])     # First planet: Mercury
print(planets[-1])    # Last planet: Neptune
print(planets[-2])    # Second to last: Uranus

# Indexing into nested lists:
print(hands[0])       # First hand: ['J', 'Q', 'K']
print(hands[0][1])    # Second card of first hand: 'Q'


# ------------------------------------------------------------------
# 2. Slicing (Grabbing a portion of a list)
# ------------------------------------------------------------------
# Syntax: list[start : end]  (includes start, stops BEFORE end)

print("2. Slicing Examples:")
print(planets[0:3])   # First 3 planets: ['Mercury', 'Venus', 'Earth']
print(planets[:3])    # Shortcut: omitting start defaults to 0
print(planets[3:])    # From index 3 to the end: ['Mars', 'Jupiter', ...]
print(planets[1:-1])  # Everything except first and last planet
print(planets[-3:])   # The last 3 planets: ['Saturn', 'Uranus', 'Neptune']

# ------------------------------------------------------------------
# 3. Changing lists (Lists are Mutable)
# ------------------------------------------------------------------
# You can modify individual elements or entire slices:

print("3. Changing Lists Examples:")
# Modify a single element:
planets[3] = 'Malacandra'  # Rename Mars
print(planets[3])          # Malacandra

# Modify a slice (replace the first 3 planets with shorter names):
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets[:4])         # ['Mur', 'Vee', 'Ur', 'Malacandra']

# Restore original names:
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']

# ------------------------------------------------------------------
# 4. List Functions
# ------------------------------------------------------------------
# Python has general built-in functions that work on lists:

print("4. List Functions Examples:")
# len(): count total elements
print(len(planets))  # 8

# sorted(): returns a new list sorted alphabetically (original unchanged)
print(sorted(planets))

# Math functions on a list of numbers:
primes = [2, 3, 5, 7, 11]
print(sum(primes))  # 28 (2 + 3 + 5 + 7 + 11)
print(max(primes))  # 11
print(min(primes))  # 2

# ------------------------------------------------------------------
# 5. Interlude: Objects
# ------------------------------------------------------------------
# In Python, *everything* is an object!
# Objects carry two things:
# 1. Attributes: data/metadata stored inside the object (accessed with dot: obj.attr)
# 2. Methods: functions attached to the object (called with parentheses: obj.method())

print("5. Interlude: Objects Examples:")
x = 12
# An int has attributes:
print(x.imag)           # Imaginary part of a number: 0
# An int has methods:
print(x.bit_length())   # Number of bits needed to represent 12 in binary (1100): 4

# ------------------------------------------------------------------
# 6. List Methods
# ------------------------------------------------------------------
# Methods are functions specifically attached to list objects:

print("6. List Methods Examples:")
# .append(): adds an item to the end of the list (modifies list in place)
planets.append('Pluto')
print(planets[-1])   # Pluto

# .pop(): removes and returns the last item
popped_planet = planets.pop()
print(popped_planet) # Pluto

# 'in' operator: checks if an item is inside the list
print('Earth' in planets)  # True
print('Pluto' in planets)  # False

# .index(): returns the position of an item
print(planets.index('Earth'))  # 2

# ------------------------------------------------------------------
# 7. Tuples
# ------------------------------------------------------------------
# Tuples are almost identical to lists, but defined using parentheses ():
# KEY DIFFERENCE: Tuples are IMMUTABLE (cannot be modified after creation).

print("7. Tuples Examples:")
t = (1, 2, 3)
print(t)

# Trying to change t[0] = 99 will raise a TypeError!

# Great use case 1: Functions returning multiple values
x = 0.125
numerator, denominator = x.as_integer_ratio()  # Returns tuple (1, 8)
print(numerator, denominator)                  # 1 8

# Great use case 2: Swapping two variables in one clean line
a = 1
b = 2
a, b = b, a   # Unpacks tuple (b, a) into (a, b)
print(a, b)   # 2 1

# --- Run Command ---
# python3 01-python/05_lists.py

# --- Output ---
# 1. Indexing Examples:
# Mercury
# Neptune
# Uranus
# ['J', 'Q', 'K']
# Q

# 2. Slicing Examples:
# ['Mercury', 'Venus', 'Earth']
# ['Mercury', 'Venus', 'Earth']
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
# ['Saturn', 'Uranus', 'Neptune']
# 3. Changing Lists Examples:
# Malacandra
# ['Mur', 'Vee', 'Ur', 'Malacandra']
# 4. List Functions Examples:
# 8
# ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
# 28
# 11
# 2
# 5. Interlude: Objects Examples:
# 0
# 4
# 6. List Methods Examples:
# Pluto
# Pluto
# True
# False
# 2
# 7. Tuples Examples:
# (1, 2, 3)
# 1 8
# 2 1
