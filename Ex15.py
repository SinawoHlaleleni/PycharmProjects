
#here you have to create a new file mine is called ex15_sample.txt so
# that you can run this python file. eg. python Ex15.py ex15_sample.txt.
from sys import argv

script, filename = argv

txt = open(filename)

print("Here is my filename{}: ".format(filename))
print(txt.read())

print("Typ the filename again: ")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
