# Exercise 5: More Variables and Printing
# https://learnpythonthehardway.org/python3/ex5.html

my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy'")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usuall {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and my {my_weight} I get {total}")


def convert_in_to_cm(inches):
    return print("Height converted from inches to centimeters:",
                 round(inches * 2.54, 1), "cm")


def convert_lbs_to_kilos(lbs):
    return(print("Pounds convert to kilograms:",
                 round(lbs * 0.453592, 1), "kg"))


convert_in_to_cm(my_height)
convert_lbs_to_kilos(my_weight)
