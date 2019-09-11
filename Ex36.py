from sys import argv
from sys import exit


script, first, second, third, fourth, fifth = argv

print("The script is called: ", script)
print("Sinawo is belong to the first list called: ", first)
print("And You the following one:", second)
print("So that the next person could be : ",third)
print("Then i will know the following is the last one:", fourth)
print("Yess am the last one:", fifth)

#This is as list

shoezy = [" 1. Training Shoes", " 2. Adidas Flops", " 3. Run First\n"]

for i in shoezy:

    print(f"\nList of shoes  {i} ")

print("""you choose one it's 1, 2 or 3  """)


def gold_room():
    print("This room is full of Training shoes, you already chose yours!.Keep them safe")

shoes = input(" > ")

if shoes == "1":
    print("Thalaaah you got your self training shoes")
    print("What you gonna do with them?")
    print("1. Wear them to Jog.")
    print("2. Wear them in the rain.")
    print("3. Wear the to go to hiking.")
    print("4. Hide them for their look.")

    training = input(" > ")

    if training == "1":
        print("Standing a chance to win another price!... Good job!.")
    elif training == "2":
        print("You will lose them very early,  Kind of bad!.")
    elif training == "3":
        print("Good idea they having more than expected balance... Good job indeed!.")
    elif training == "4":
        gold_room()


if shoes == "2":
    print("Hello there you won your self an Adidas brand flops")
    print("1. Use them as sleepers.")
    print("2. Wear them for summer sun.")
    print("3. Don't wear them at all.")


#def just_room():
    #print("Then there's this one full of Adidas brands, you chose yours keep them safe!")

    adidas = input(" > ")

    if adidas == "1":
        print("Your shoes will feet you very well .")
    elif adidas == "2":
        print("which is a good idea...")
    elif adidas == "3":
        print("Then there's this one")
        #just_room()


if shoes == "3":
    print("Hello there you won your self run first")
    print("1. Use them as sleepers.")
    print("2. hide them in front of the people.")
    print("3. Wear them during shower time or as backup.")


    #def funny_room():
        #print("And there's this one full of funny shoes but great, you chose yours keep them safe!")

    runny = input(" > ")

    if runny == "1":
        print("You will feel cold feet .")
    elif runny == "2":
        print("That would be a challenge to your self ")
    elif runny == "3":
        print("And there's this one")
    #funny_room()


else:
    print("We do not recognise that option, Try to choose the right option")
