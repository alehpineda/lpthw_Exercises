# f-string x
types_of_people = 10
x = f"There are {types_of_people} types of people."

# f-string y
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print x and y
print(x)
print(y)

# print x and y again
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Bool
hilarious = False

# Eval joke
joke_evaluation = "Isn't that joke so funny?! {}"
# Print eval joke
print(joke_evaluation.format(hilarious))

# Sum 2 strings
w = "This is the left side of ..."
e = "a string with a right side."

# Concatenate
print(w + e)
