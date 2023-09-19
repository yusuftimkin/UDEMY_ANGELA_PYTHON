
bill = float(input("How much is the bill?\n"))
num_people = int(input("How many people was in the dinner?\n"))
tip = int(input("what is the percentage of tip?\n"))

bill_person = (bill / num_people) * (tip /100 + 1) 

print(f'{bill_person:.2f} US Dollars')
