import random

people = int(input("How many people do you have? "))
lst = []

for i in range(people):
    name = input("Enter name:")
    lst.append(name)

random_index = random.randint(0, len(lst) - 1)
payer = lst[random_index]
print(f"{payer} pays today!")
