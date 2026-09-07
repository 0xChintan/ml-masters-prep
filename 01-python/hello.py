# 1. Start with 0
spam_amount = 0
print(spam_amount)

# 2. Add 4 more (so it becomes 4)
spam_amount = spam_amount + 4

# 3. If it is greater than 0, print the message
if spam_amount > 0:
    print("But I don't want ANY spam!")

# 4. Concept: In Python, multiplying text by a number repeats it!
# Instead of math, "Spam " * 4 just writes "Spam " 4 times.
viking_song = "Spam " * spam_amount
print(viking_song)

# --- Output ---
# 0
# But I don't want ANY spam!
# Spam Spam Spam Spam 