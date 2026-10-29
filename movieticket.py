number_of_people=int(input("Number of People:"))
for person in range(number_of_people):
    name=input("What is your NAME:")
    age=int(input("What is your age:"))
if age<15:
    value=80
elif age>65:
    value=100 
else:
    value=150
total_amount=number_of_people*value
print("-----MOVIE TICKET RECIEPT-----")
print("Toatal people", number_of_people)
print("Total Amount:", total_amount)
