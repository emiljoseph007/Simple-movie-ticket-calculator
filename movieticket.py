number_of_people = int(input("Number of people: "))
names = []
total_ticket_amount = 0

for person in range(number_of_people):
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    names.append(name)

    if age < 15:
        ticket_price = 80
    elif age > 65:
        ticket_price = 100
    else:
        ticket_price = 150

    total_ticket_amount += ticket_price

snacks = input("Do you want any snacks? ").strip().lower()
popcorn = 0
pepsi = 0

if snacks == "yes":
    popcorn = int(input("How many popcorn: "))
    pepsi = int(input("How many Pepsi: "))
else:
    print("No snacks selected")

popcorn_total = popcorn * 20
pepsi_total = pepsi * 30
total_snack_amount = popcorn_total + pepsi_total
grand_total = total_ticket_amount + total_snack_amount

print("----- MOVIE TICKET RECEIPT -----")
print("Names:", ", ".join(names))
print("Total people:", number_of_people)
print("Popcorn:", popcorn)
print("Pepsi:", pepsi)
print("Total snacks:", popcorn + pepsi)
print("Ticket price total: Rs", total_ticket_amount)
print("Snack price total: Rs", total_snack_amount)
print("Grand total: Rs", grand_total)