number_of_people = int(input("How many people: "))
names = []
total_amount = 0

for person in range(number_of_people):
    name = input("What's your name: ")
    age = int(input("What is your age: "))
    names.append(name)
    if age < 13:
        value = 150
    elif age > 60:
        value = 200
    else:
        value = 350
    total_amount += value

print("-----MOVIE TICKET RECEIPT-----")
print("Names:", ", ".join(names))
print("Number of people:", number_of_people)
print("Total Amount:", total_amount)