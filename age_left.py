age = input("What is your current age? ")

age_left = 90 - int(age)

x = age_left * 365
y = age_left * 52
z = age_left * 12

print(f"You have {x} days, {y} weeks, and {z} months left.")