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


# Find the Perimeter of a Rectangle
def find_perimeter(height, width):
    return height * 2 + width * 2


# Count the Syllables
def count_syllables(txt):
    count = 0
    for letter in txt.lower():
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


def count_syllables2(txt):
    return len([x for x in txt.lower() if x in 'aeiou'])


def count_syllables3(txt):
    return sum(1 for i in txt.lower() if i in 'aeiou')


# Get the Sum of All List Elements
def get_sum_of_elements(lst):
    return sum(lst)


# Is the Last Character an N?
def is_last_character_n(word):
    return word[len(word) - 1] in 'nN'


def hello_world(num):
    if not num % 15: return 'Hello World'
    if not num % 3: return 'Hello'
    if not num % 5: return 'World'


def greater_than_one(frac):
    return (int(frac.split("/")[0]) / int(frac.split("/")[1])) > 1


# faster python way
# def greaterThanOne(frac):
#     return eval(frac) > 1

def googlify(n):
    if n < 2:
        return "invalid"
    return "G" + n * "o" + "gle"


# def googlify(n):
# 	return 'G{}gle'.format('o'*n) if n > 1 else 'invalid'

def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    return False


# def is_triangle(*sides):
#     return all(s < sum(sides) - s for s in sides)


def pH_name(pH):
    if pH < 0 or pH > 14:
        return "invalid"
    return "acidic" if 7 > pH else "alkaline" if pH > 7 else "neutral"


def detect_word(txt):
    return "".join([let for let in txt if let.lower() == let])


# def detect_word(txt):
# 	return "".join(c for c in txt if c.islower())

def skip_the_sugar(drinks):
    return [drink for drink in drinks if drink not in ['fanta', 'cola']]


def has_hidden_fee(prices, t):
    return (sum(int(price.strip("$")) for price in prices)) < int(t.strip("$"))


def my_func(string):
    return [s for s in string if s.isnumeric()], [s for s in string if s.isalpha()]


def add_odd_to_n(n):
    return sum(num for num in range(n + 1) if num % 2 != 0)


def Long_Burp(num):
    return "Bu" + num * "r" + "p"


def eq(evaluate):
    return evaluate


def convert(letter):
    return ord(letter)


def has_same_bread(lst1, lst2):
    # return lst1[::len(lst1) - 1]
    return lst1[::len(lst1) - 1] == lst2[::len(lst2) - 1]


def is_it_true(relation):
    if "=" in relation:
        return relation.split("=")[0] == relation.split("=")[1]
    return eval(relation)


def halfQuarterEighth(n):
    return [n / 2, n / 4, n / 8]


def potatoes(potato):
    return potato.count("potato")


def backwords(str):
    return str[::-1]


def sum_first_n_nums(lst, n):
    return sum(lst[0:n])


def simplePigLatin(word):
    return word[1:] + word[0] + "ay"


def get_triangle_type(lst):
    if len(lst) > 3 or len(lst) < 3:
        return "not a triangle"
    if len(set(lst)) == 1:
        return "equilateral"
    if len(set(lst)) == 2:
        return "isosceles"
    return 'scalene'


def convert(data1, data2):
    return type(data1)(data2)


def reverse_title(txt):
    return txt.title().swapcase()


d1 = {'D': 1, 'B': 2, 'C': 3}
d2 = {'likes': 2, 'dislikes': 3, 'followers': 10}


def dict_to_list(d):
    return sorted(d.items())


def squares_sum(n):
    return sum(i ** 2 for i in range(0, n + 1))


def find_the_falsehoods(lst):
    return [i for i in lst if not i]


def is_repeated(strn):
    return strn


def reverse_list(num):
    return [int(i) for i in list(str(num))[::-1]]


def zip_it(women, men):
    return list(zip(women, men)) if len(women) == len(men) else "Sizes don't match"


def max_total(nums):
    return sum(sorted(nums)[-5:])


def is_potential_friend(set1, set2):
    return True if len(set1 & set2) >= 2 or set1 == set2 else False
    # return set1 & set2


def number_args(*argv):
    return len(argv)


def sub_reddit(link):
    return link.split('/')[-2]


def filter_unique(lst):
    return [item for item in lst if len(item) == len(set(item))]


def strip_sentence(txt, chars):
    return ''.join([char for char in txt if char not in chars])


def add_nums(nums):
    return sum(int(num) for num in nums.split(', '))


def count_ones(matrix):
    return sum([row.count(1) for row in matrix])


def length(txt):
    if len(txt) == 0:
        return 0
    return length(txt[0:-1]) + 1


def findHighest(list, higher=0):
    if len(list) == 0:
        return higher
    highest = higher
    if list[0] > highest:
        highest = list[0]
    return findHighest(list[1:], highest)


def one_odd_one_even(n):
    arr = [int(i) for i in str(n)]
    if arr[0] % 2 == 0 and arr[1] % 2 != 0:
        return True
    if arr[0] % 2 != 0 and arr[1] % 2 == 0:
        return True
    return False


def add_up(n):
    if n == 1:
        return n
    else:
        return n + add_up(n - 1)




print(add_up(4))
print(add_up(1000))
