
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
i = 0
for animal in animals:
    print(f"The animal at {animals} is {animal}")
    print(f"The animal at 1 is  {animal}")


while i < 6:
    print(f"At the top i is {i}")
    animals.append(i)

    i = i + 1
    print(f"At the bottom i is {i}")