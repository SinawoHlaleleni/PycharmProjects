
#To run this you have to run it in command and by typing {python
# (name of project) and three arguments eg, python ex13.py Fruit Sweets Veg}
from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)