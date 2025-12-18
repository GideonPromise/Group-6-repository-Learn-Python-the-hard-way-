# Exercise 10. Escape Codes in Strings

# Create a variable with \t (tab) escape code to indent the text
tabby_cat = "\tI'm tabbed in."

# Create a variable with \n (newline) escape code to split text across two lines
persian_cat = "I'm split\non a line."

# Create a variable with \\ (backslash) escape code to print actual backslashes
backslash_cat = "I'm \\ a \\ cat."

# Create a multi-line string using triple quotes with multiple escape codes
# \t creates tabs for indentation, \n creates new lines
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Print the tabbed cat string (text will be indented)
print(tabby_cat)

# Print the split cat string (text will appear on two lines)
print(persian_cat)

# Print the backslash cat string (backslashes will be visible)
print(backslash_cat)

# Print the fat cat multi-line string with tabs and newlines
print(fat_cat)


# Exercise 11. Asking People Questions

# Print a question prompt without a newline at the end (end=' ' keeps it on same line)
print("How old are you?", end=' ')

# Wait for user to type their age and press Enter, then store it in the age variable
age = input()

# Print a height question prompt without a newline at the end
print("How tall are you?", end=' ')

# Wait for user to type their height and press Enter, then store it in the height variable
height = input()

# Print a weight question prompt without a newline at the end
print("How much do you weigh?", end=' ')

# Wait for user to type their weight and press Enter, then store it in the weight variable
weight = input()

# Use f-string formatting to print a summary sentence with all the user's input values
print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# Exercise 12. An Easier Way to Prompt

# Ask for age using input() with the prompt built-in (simpler than Exercise 11)
age = input("How old are you? ")

# Ask for height using input() with the prompt built-in
height = input("How tall are you? ")

# Ask for weight using input() with the prompt built-in
weight = input("How much do you weigh? ")

# Print a summary using regular string formatting (NOT f-string, so variables won't be inserted)
# BUG: This should use f"..." to actually insert the values
print("So, you're {age} old, {height} tall and {weight} heavy.")
