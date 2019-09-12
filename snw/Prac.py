print("\n EXC 1")
print("\n hello world")
print("hello again")
print("I like what i do")
print("It is fun")

print("\n EXC 2")
...

print("\n EXC 3 NUMBERS AND MATH")

print("\n me", 25 + 30/6)
print("yeah", 100 - 25 * 3 % 4)

print("\n True / false ")

print(3 + 2 < 5 - 7)
print(3 + 2 > 5 - 7)

print(5 >= -2)
print(5 <= -2)

print("\n EXC 4 VARIABLES AND NAMES")

cars = 100
driver = 30
passenger = 90
hired = "NDs"
carpool_capacity = cars + driver

print(" There are ", cars, "Available")
print("There are only", driver, "driver available")
print("We have", passenger, "to carpool today")
print("we", hired,"to deliver")
print("There are",carpool_capacity, "people today")

print("\n EXC 5 More VARIABLES AND PRINTING")

my_name = 'S N W'
My_age = 35
My_height = 74
My_weight = 180
My_eyes = 'Black'
My_teeth = 'White'
My_hair = 'Lemon'

print("\n Let's talk about {}.".format(my_name))
print("He's {} inches tall.".format(My_height))
print("He's {} pounds heavy.".format(My_weight))
print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.".format(My_eyes, My_hair))
print("His teeth are usually {} depending on the coffee". format(My_teeth))

total = My_age + My_height + My_weight
print("If I add {}, {}, and {} I get {}.".format(My_age, My_height, My_weight, total))

print("\n EXC 6 STRINGS AND TEXT")

type_of_people = 10
x = "\n There are {} types of people.".format(type_of_people)

binary = "binary"
do_not = "don't"
y = "Those who know {} and those who {}.".format(binary, do_not)

print(x)
print(y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of "
e = "a string with a right side."

print(w + e)

print("\n EXC 7")
...

print("\n EXC 8 FORMATING A STRING... LITTLE BIT CONFUSED")

formatter = " \n {} {} {} {} {}"

print(formatter.format(1, 2, 3, 4,5))
print(formatter.format("one", "two", "three", "four", "five"))
print(formatter.format(True, False, False, True, True))
print(formatter.format(formatter, formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear!",
    "Yes i tried \n",
))
print ("\n EXC 9 ...\n ")
days = " Mon Tue Wed Thur Fri Sat Sun\n"
months = "\n Jan \n Feb \n Mar \n Apr \n May \n Jun \n Jul \n Aug \n ..."

print(days)
print(months)
print("These are the {} and \n also the {} \n of the year".format(days, months))
print("""

There will be difficult times.
With happy days as well.
.......
    
""")

print("\n EXC 10")
...

print(" exc 11 GETTING DATA FROM PROGRAM\n")

#date_of_birth = input("Birth year")
#age = 2019 - int(date_of_birth)
#print(age)

print("birth Year: ", end='')
year_of_birth = input()
age = 2019 - int(year_of_birth)
#print(age)

print("How old are you?  :", end='')
print(age)
#age = input(age)
print("What is your weight in lbs? :", end='')
weight = input()
print("And what your height is?  :",end='')
height =input()

print("Here are my details,i was born in {}, am age of {}, weight  {} and height is {}".format(year_of_birth,age, weight, height))

print(" \n exc 12 PROMPTING POEPLE\n")
age = input("How old are you?  ")
height = input("How tall are you? ")
print("So, you are {} old and {} tall".format(age, height))


