
from sys import argv

script, user_name = argv
prompt = ' > '

print("Hi {}, I'm the {}script".format(user_name, script))
print("I'd like to ask you a few question.")
print("Do you like me {}?".format(user_name))
likes = input(prompt)

print("Where do you live {}".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
so you said {} about liking me , you live in {} and your computer is {} 

""".format(likes, lives, computer))

