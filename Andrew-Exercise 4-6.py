# Exercise 4: This exercise deals with Variables and Names

# numbers of Cars that are available
cars = 100

# these are the available spaces per car
space_in_a_car = 4.0

# number of available drivers
drivers = 30

# this is the number of passagers in total
passagers = 90

# number of cars that are not to be driven 
cars_not_driven = cars - drivers

# number of cars with available drivers per car
cars_driven = drivers

# number of load(i.e. people) that the driven cars can transport
carpool_capacity = cars_driven * space_in_a_car

# mean number of passagers for each car(i.e. average)
average_passagers_per_car = passagers / cars_driven

# Output display
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people todat.")
print("We have", passagers, "to carpool today.")
print("We need to put about", average_passagers_per_car, "in each car.")



# Exercise 5: This exercise deals with More Variables and Printing

# My full name is here
my_name = 'Ayeyemi O, Andrew'

# My age in the next four months
my_age = 18 # not a lie

# This how tall I am
my_height = 74 # inches

# How much I weigh
my_weight = 170 # lbs

# The color of My eye balls
my_eyes = 'blue'

# The color of my teeth
my_teeth = 'white'

# The revealed color of my hair
my_hair = 'black'

# Output display
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This Line is a little tricky
print(f"If I add {my_age}, {my_height}, and {my_weight}")



# Exercise 6: This part deals with the title Strings and Text

# Types of people in a digit format (number of types of people)
types_of_people = 10

# f-String: Insert the types of people into a string
x = f"There are {types_of_people} types_of_people."

# Two String variables
binary = "binary"
do_not = "don't"

# Another f-string with two variables
y = f"Those who know {binary} and those who {do_not}."

# Output display of string
print(x)
print(y)

# Output display inscribed inside other strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# A boolean expression (True or False) 
hilarious = False

# String with a placeholder for a format()
joke_evaluation = "Isn't that joke so funny?! {}"

# Output display
print(joke_evaluation. format(hilarious))

# Two input Strings Values
w = "This is the left of..."
e = "a string with a right side."

# Output display joining two string values together
print(w + e)