# Challenges

# Shapes with N sides

# Create a function that takes a whole number as input and returns the shape with that number's amount of sides. Here are the expected outputs to get from these inputs.
#
# Inputs	Outputs
# 1	"circle"
# 2	"semi-circle"
# 3	"triangle"
# 4	"square"
# 5	"pentagon"
# 6	"hexagon"
# 7	"heptagon"
# 8	"octagon"
# 9	"nonagon"
# 10	"decagon"
# Examples
# n_sided_shape(3) ➞ "triangle"
#
# n_sided_shape(1) ➞ "circle"
#
# n_sided_shape(9) ➞ "nonagon"

def n_sided_shape(n):
    shape_dict = {
        1: "circle",
        2: "semi-circle",
        3: "triangle",
        4: "square",
        5: "pentagon",
        6: "hexagon",
        7: "heptagon",
        8: "octagon",
        9: "nonagon",
        10: "decagon"
    }
    return shape_dict[n]


# Formatting text on edabit

# The important thing when a comment is posted on Edabit is its content. But when a comment is formatted in the right way, it will be properly shown and it will be easily readable by everyone.
#
# In this challenge, you have to format a word using four specific methods of the Markdown language that is used by Edabit to format the text in the Comments tab and the Instructions tab (during the creation, or the translation, of a challenge). Each of these four methods (or styles) is identified by the lowercased initial letter of its name:
#
# "b" is for bold
# "i" is for italics
# "c" is for inline code
# "s" is for strikethrough
# You are given two parameters: a string word being the word to format, and another string style being the lowercased initial of the style to apply. You have to implement a function that returns a string being the word surrounded by the special characters used to apply the given style.


def md_format(word, style):
    if style == 'b':
        return "**" + word + "**"
    if style == 'i':
        return "_" + word + "_"
    if style == "c":
        return '`' + word + '`'
    if style == "s":
        return "~~" + word + "~~"


# How Many Decimal Places?

# Create a function that returns the number of decimal places a number has. Any zeros after the decimal point count towards the number of decimal places.
#
# Examples
# get_decimal_places("43.20") ➞ 2
#
# get_decimal_places("400") ➞ 0
#
# get_decimal_places("3.1") ➞ 1


def get_decimal_places(n):
    if "." not in n:
        return 0
    return len(n.split(".")[1])


# Aging the population

def after_n_years(names, n):
    return {name: age + abs(n) for (name, age) in names.items()}


# Clear the fog

def clear_fog(txt):
    if not any(x in txt for x in "fog"):
        return "It's a clear day!"
    fog = "fog"
    word = txt
    for char in fog:
        word = word.replace(char, "")
    return word




